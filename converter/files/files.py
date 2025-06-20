import utils
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from converter.files.files_api import file_converter_api


class FilesConverterApi:

    def __init__(self):
        self.router = APIRouter(prefix='/files', tags=['FilesConverter'])
        self.templates = Jinja2Templates(directory="templates")
        self.context: dict = {}

        @self.router.get("", response_class=HTMLResponse, name='files_converter')
        async def files_converter(request: Request, limit: int = 6):
            cat_num = 5
            filter_pages = utils.select_converter_pages_by_category(cat_num, limit)

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="files.html", context={'links': filter_pages,
                                                            'title': 'Конвертеры файлов ',
                                                            'h1': 'Конвертеры файлов',
                                                            'page': 'files',
                                                            'tags': ('Pdf',
                                                                     'Docx',
                                                                     'Jpeg',
                                                                     'Png',
                                                                     'Ico',
                                                                     'Heic',
                                                                     'WebP',
                                                                     'Tiff'),
                                                            'category': cat_num})


files_converter_api = FilesConverterApi()
files_converter_api.router.include_router(file_converter_api.router)