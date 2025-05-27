import os
import uuid
import fitz
from PIL import Image
from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request, UploadFile, File
from starlette.templating import Jinja2Templates


class PdfApi:

    def __init__(self):
        self.router = APIRouter(prefix='/pdf', tags=['Pdf'])
        self.templates = Jinja2Templates(directory="templates")
        self.context: dict = {}
        self.upload_dir: str = 'uploads'

        @self.router.post("/upload/")
        async def upload_file(file: UploadFile = File(...)):

            # Генерируем уникальное имя файла
            file_id = str(uuid.uuid4())
            # Получил разрешение
            file_ext = os.path.splitext(file.filename)[1]
            file_path = os.path.join(self.upload_dir, f"{file_id}{file_ext}")

            # Сохраняем файл
            with open(file_path, "wb") as buffer:
                buffer.write(await file.read())

            # Возвращаем ссылку
            return {"file_url": f"/static/{file_id}{file_ext}"}

    @staticmethod
    async def pdf_to_jpeg(pdf_path, output_folder, img_fmt: str, dpi=300):
        """
        Конвертирует PDF в JPEG изображения (по одной странице на файл)

        :param img_fmt: Формат конвертируемого изображения
        :param pdf_path: Путь к PDF файлу
        :param output_folder: Папка для сохранения JPEG
        :param dpi: Качество изображения (300 по умолчанию)
        """
        # Создаем папку, если её нет
        os.makedirs(output_folder, exist_ok=True)

        # Открываем PDF
        pdf_document = fitz.open(pdf_path)

        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)

            # Конвертируем страницу в изображение (пиксельная карта)
            pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72))

            # Создаем изображение Pillow из данных
            img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)

            # Сохраняем как JPEG
            output_path = os.path.join(output_folder, f"page_{page_num + 1}.jpg")
            img.save(output_path, img_fmt, quality=95)

            print(f"Страница {page_num + 1} сохранена как {output_path}")

        pdf_document.close()
        print(f"Конвертация завершена! Файлы сохранены в {output_folder}")


class PdfFunc:
    def __init__(self, api, link):
        self.api: PdfApi = api
        self.router = APIRouter(prefix='/' + link, tags=[link])

        @api.router.get('/' + link + '/', response_class=HTMLResponse, name='pdf_to_' + link)
        async def new_func(request: Request):
            self.api.context['title'] = 'Pdf в ' + link.capitalize() + ' конвертер'
            # await self.api.pdf_to_jpeg(img_fmt=link.upper(), pdf_path='', output_folder=self.api.upload_dir)

            # Получить данные
            return self.api.templates.TemplateResponse(
                request=request, name="converter/files_converter.html", context=self.api.context)


pdf_to_img_api = PdfApi()
pdf_to_img_api.router.include_router(PdfFunc(api=pdf_to_img_api, link='jpeg').router)