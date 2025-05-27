import utils
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from converter.files.pdf import pdf_to_img_api


class FilesConverterApi:

    def __init__(self):
        self.router = APIRouter(prefix='/files', tags=['FilesConverter'])
        self.templates = Jinja2Templates(directory="templates")
        self.context: dict = {}

        @self.router.get("", response_class=HTMLResponse, name='files_converter')
        async def files_converter(request: Request, limit: int = 6):

            filter_pages = utils.select_main_pages_by_category(5, limit)

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="home.html", context={'links': filter_pages,
                                                            'title': 'Конвертеры файлов | ',
                                                            'h1': 'Конвертеры файлов'})


files_converter_api = FilesConverterApi()
files_converter_api.router.include_router(pdf_to_img_api.router)