import json
import os
import fitz
import pillow_heif
from PIL import Image
from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request, UploadFile, File
from starlette.templating import Jinja2Templates

from converter.files.texts import Pdf, Jpeg, Docx


class ConverterApi:

    def __init__(self):
        self.router = APIRouter(prefix='', tags=['Converter'])
        self.templates = Jinja2Templates(directory="templates", auto_reload=True)

    # Проверить валидность изображения
    @staticmethod
    def is_valid_image_pillow(file_name):
        try:
            with Image.open(file_name) as img:
                img.verify()
                return True
        except (IOError, SyntaxError):
            return False

    @staticmethod
    async def convert_heic(filename: str, output_folder: str, img_fmt: str, filepath: str, new_images: list):

        heif_file = pillow_heif.read_heif(filepath)
        img = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
        )

        new_filename = f"{filename.split('.')[0]}.{img_fmt}"
        output_path = os.path.join(output_folder, new_filename)
        img.save(output_path, img_fmt, quality=95)
        new_images.append(new_filename)

    @staticmethod
    async def convert_few_type(filename: str, output_folder: str, img_fmt: str, filepath: str, new_images: list):

        new_document = fitz.open(filepath)

        for page_num in range(len(new_document)):
            page = new_document.load_page(page_num)

            # Конвертируем страницу в изображение (пиксельная карта)
            pix = page.get_pixmap(matrix=fitz.Matrix(300 / 72, 300 / 72))

            # Создаем изображение Pillow из данных
            img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)

            # Сохраняем как JPEG
            new_filename = f"{filename.split('.')[0]}_{page_num + 1}.{img_fmt}"
            output_path = os.path.join(output_folder, new_filename)
            new_images.append(new_filename)
            img.save(output_path, img_fmt, quality=95)

            print(f"Страница {page_num + 1} сохранена как {output_path}")

        new_document.close()

    async def convert_to_pdf(self, from_format: str, new_files: list, unite_files: bool = True):
        """
        Функция для конвертации файлов в PDF
        :param from_format:
        :param new_files:
        :param unite_files:
        :return:
        """
        if from_format == 'heic':

            jpg_files = []
            for file in new_files:
                filename = os.path.basename(file)
                filepath = os.path.join('uploads', filename)
                await self.convert_heic(filepath=filepath,
                                        filename=filename,
                                        new_images=jpg_files,
                                        img_fmt='jpeg',
                                        output_folder='output')
            file_paths = [os.path.join('output', os.path.basename(file)) for file in jpg_files]

        else:
            file_paths = [os.path.join('uploads', os.path.basename(file)) for file in new_files if
                          self.is_valid_image_pillow(os.path.join('uploads', os.path.basename(file)))]

        images = [Image.open(f) for f in file_paths]

        if unite_files:
            new_name = os.path.basename(new_files[0]).split('.')[0] + '.pdf'
            output_path = os.path.join('output', new_name)
            images[0].save(output_path, save_all=True, append_images=images[1:])
            return [new_name]
        else:
            new_files = []
            for file in images:
                new_name = os.path.basename(file.filename).split('.')[0] + '.pdf'
                output_path = os.path.join('output', new_name)
                file.save(output_path)
                new_files.append(new_name)
            return new_files


    async def convert_file(self, filename: str, output_folder: str, img_fmt: str, ext: str):
        """
        Конвертирует один или несколько файлов в зависимости от типа

        :param filename: Наименвоание файла на сервере
        :param img_fmt: Формат конвертируемого изображения
        :param output_folder: Папка для сохранения JPEG
        :param ext: Расширение входящего файла
        :param dpi: Качество изображения (300 по умолчанию)
        """

        # Создаем папку, если её нет
        os.makedirs(output_folder, exist_ok=True)
        # Открываем PDF
        filepath = os.path.join('uploads', filename)

        new_images = []
        params = {'filename': filename,
                  'filepath': filepath,
                  'img_fmt': img_fmt,
                  'output_folder': output_folder,
                  'new_images': new_images}

        if ext == 'heic':
            await self.convert_heic(**params)
        else:
            await self.convert_few_type(**params)

        return new_images


class ConverterFunc:
    def __init__(self, api):

        self.api: ConverterApi = api
        self.router = APIRouter(prefix='/convert')
        self.formats = ('pdf', 'docx', 'jpeg', 'png', 'bmp', 'heic', 'webp', 'tiff')

        @api.router.get('/', response_class=HTMLResponse, name='files')
        async def files(request: Request, ff: str, tf: str):

            ff_cap = ff.capitalize()
            tf_cap = tf.capitalize()

            main_texts = {
                          'pdf': Pdf,
                          'jpeg': Jpeg,
                          'docx': Docx,
                          # 'heic': Heic,
                          # 'webp': WebP,
                          # 'png': Png,
                          # 'tiff': Tiff,
                         }

            context = {'title': ff_cap + ' в ' + tf_cap + ' конвертер онлайн без регистрации',
                       'h1': f'Преобразовать {ff_cap} в {tf_cap} онлайн',
                       'ff': ff_cap,
                       'tf': tf_cap,
                       'ff_txt': main_texts.get(ff, 'Описание исходного формата'),
                       'tf_txt': main_texts.get(tf, 'Описание требуемого формата'),
                       'formats': self.formats
                       }

            # Получить данные
            return self.api.templates.TemplateResponse(
                request=request, name="converter/files_converter.html", context=context)

        @api.router.post('/', response_class=HTMLResponse)
        async def convert(request: Request, ff: str, tf: str):

            result = {}
            result['new_images'] = []
            result['img_fmt'] = tf.capitalize()

            data = await request.json()
            file_urls = data.get('file_urls')
            unite_files = data.get('unite_files')

            try:
                if tf == 'pdf':
                    new_pdf = await self.api.convert_to_pdf(from_format=ff, new_files=file_urls, unite_files=unite_files)
                    result['new_images'].append(new_pdf)
                else:
                    for url in file_urls:
                        filename = os.path.basename(url)
                        new_images = await self.api.convert_file(img_fmt=tf,
                                                                 filename=filename,
                                                                 output_folder='output',
                                                                 ext=ff)
                        result['new_images'].append(new_images)

            except Exception as E:
                result['error'] = f'Ошибка! Загрузите файл в формате {ff.capitalize()}.'

            return json.dumps(result)


file_converter_api = ConverterApi()
file_converter_api.router.include_router(ConverterFunc(api=file_converter_api).router)
