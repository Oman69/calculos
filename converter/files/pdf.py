import json
import os
import fitz
from PIL import Image
from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request, UploadFile, File
from starlette.templating import Jinja2Templates


class ConverterApi:

    def __init__(self):
        self.router = APIRouter(prefix='', tags=['Converter'])
        self.templates = Jinja2Templates(directory="templates")

    @staticmethod
    async def pdf_to_jpeg(filename: str, output_folder, img_fmt: str, dpi=300):
        """
        Конвертирует PDF в JPEG изображения (по одной странице на файл)

        :param filename: Наименвоание файла на сервере
        :param img_fmt: Формат конвертируемого изображения
        :param output_folder: Папка для сохранения JPEG
        :param dpi: Качество изображения (300 по умолчанию)
        """
        # Создаем папку, если её нет
        os.makedirs(output_folder, exist_ok=True)
        # Открываем PDF
        filepath = os.path.join('uploads', filename)
        pdf_document = fitz.open(filepath)

        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)

            # Конвертируем страницу в изображение (пиксельная карта)
            pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72))

            # Создаем изображение Pillow из данных
            img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)

            # Сохраняем как JPEG
            output_path = os.path.join(output_folder, f"{filename.split('.')[0]}_{page_num + 1}.{img_fmt}")
            img.save(output_path, img_fmt, quality=95)

            print(f"Страница {page_num + 1} сохранена как {output_path}")

        pdf_document.close()


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
            filename = os.path.basename(data)
            try:
                await self.api.pdf_to_jpeg(img_fmt=tf, filename=filename, output_folder='output')
                result['message'] = "Конвертация завершена!"
            except Exception as E:
                result['message'] = 'Ошибка: ' + str(E)

            return json.dumps(result)

            # Получить данные
            # return self.api.templates.TemplateResponse(
            #     request=request, name="converter/files_converter.html", context={})


pdf_to_img_api = ConverterApi()
pdf_to_img_api.router.include_router(ConverterFunc(api=pdf_to_img_api, ff='pdf', tf='jpeg').router)
pdf_to_img_api.router.include_router(ConverterFunc(api=pdf_to_img_api, ff='pdf', tf='png').router)