import json
import os
import fitz
import pillow_heif
from PIL import Image
from pymupdf import EmptyFileError
from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request, UploadFile, File
from starlette.templating import Jinja2Templates


class ConverterApi:

    def __init__(self):
        self.router = APIRouter(prefix='', tags=['Converter'])
        self.templates = Jinja2Templates(directory="templates", auto_reload=True)

    @staticmethod
    async def convert_heic(filename: str, output_folder: str, img_fmt: str, filepath: str, new_images: list):

        heif_file = pillow_heif.read_heif(filepath)
        img = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
        )

        output_path = os.path.join(output_folder, f"{filename.split('.')[0]}.{img_fmt}")
        img.save(output_path, img_fmt, quality=95)
        new_images.append(f"{filename.split('.')[0]}.{img_fmt}")

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
            output_path = os.path.join(output_folder, f"{filename.split('.')[0]}_{page_num + 1}.{img_fmt}")
            new_images.append(f"{filename.split('.')[0]}_{page_num + 1}.{img_fmt}")
            img.save(output_path, img_fmt, quality=95)

            print(f"Страница {page_num + 1} сохранена как {output_path}")

        new_document.close()

    async def convert_to_pdf(self, filename: str, output_folder, img_fmt: str, ext: str):
        pass

    async def convert_file(self, filename: str, output_folder, img_fmt: str, ext: str):
        """
        Конвертирует PDF в JPEG изображения (по одной странице на файл)

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
    def __init__(self, api, ff: str, tf: str):

        self.api: ConverterApi = api
        self.router = APIRouter(prefix='/' + ff + '-' + tf, tags=[ff + '_' + tf])

        @api.router.get('/' + ff + '-' + tf, response_class=HTMLResponse, name=ff + '_to_' + tf)
        async def new_func(request: Request):

            ff_cap = ff.capitalize()
            tf_cap = tf.capitalize()

            context = {'title': ff_cap + ' в ' + tf_cap + ' конвертер',
                       'h1': ff_cap + ' в ' + tf_cap + ' онлайн'}

            # Получить данные
            return self.api.templates.TemplateResponse(
                request=request, name="converter/files_converter.html", context=context)

        @api.router.post('/' + ff + '-' + tf, response_class=HTMLResponse)
        async def convert(request: Request):

            result = {}
            data = await request.json()
            file_urls = data.get('file_urls')
            for url in file_urls:
                filename = os.path.basename(url)
                ext = os.path.splitext(filename)[1].lower()[1:]

                if ext != ff and ext != 'jpg':
                    result['error'] = 'Загрузите файл в формате ' + ff.capitalize() + '!'
                else:
                    new_images = await self.api.convert_file(img_fmt=tf,
                                                             filename=filename,
                                                             output_folder='output',
                                                             ext=ext)
                    result['new_images'] = new_images
                    result['img_fmt'] = tf.capitalize()

            return json.dumps(result)


file_converter_api = ConverterApi()
file_converter_api.router.include_router(ConverterFunc(api=file_converter_api, ff='pdf', tf='jpeg').router)
file_converter_api.router.include_router(ConverterFunc(api=file_converter_api, ff='pdf', tf='png').router)
file_converter_api.router.include_router(ConverterFunc(api=file_converter_api, ff='pdf', tf='webp').router)
file_converter_api.router.include_router(ConverterFunc(api=file_converter_api, ff='pdf', tf='ico').router)
file_converter_api.router.include_router(ConverterFunc(api=file_converter_api, ff='pdf', tf='tiff').router)

file_converter_api.router.include_router(ConverterFunc(api=file_converter_api, ff='docx', tf='jpeg').router)
file_converter_api.router.include_router(ConverterFunc(api=file_converter_api, ff='docx', tf='png').router)
file_converter_api.router.include_router(ConverterFunc(api=file_converter_api, ff='docx', tf='webp').router)
file_converter_api.router.include_router(ConverterFunc(api=file_converter_api, ff='docx', tf='ico').router)
file_converter_api.router.include_router(ConverterFunc(api=file_converter_api, ff='docx', tf='tiff').router)

file_converter_api.router.include_router(ConverterFunc(api=file_converter_api, ff='heic', tf='jpeg').router)
file_converter_api.router.include_router(ConverterFunc(api=file_converter_api, ff='heic', tf='png').router)
file_converter_api.router.include_router(ConverterFunc(api=file_converter_api, ff='heic', tf='ico').router)
file_converter_api.router.include_router(ConverterFunc(api=file_converter_api, ff='heic', tf='tiff').router)
file_converter_api.router.include_router(ConverterFunc(api=file_converter_api, ff='heic', tf='webp').router)

file_converter_api.router.include_router(ConverterFunc(api=file_converter_api, ff='jpeg', tf='pdf').router)
