import utils
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from converter.area.centimeter import cm2_api
from converter.area.decimeter import dm2_api
from converter.area.meter import m2_api


class AreaApi:

    def __init__(self):
        self.router = APIRouter(prefix='/area', tags=['Area'])
        self.templates = Jinja2Templates(directory="templates")
        self.context: dict = {}

        @self.router.get("", response_class=HTMLResponse, name='area')
        async def distance(request: Request, limit: int = 6):

            filter_pages = utils.select_main_pages_by_category(33, limit)

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="home.html", context={'links': filter_pages,
                                                            'title': 'Единицы площади | ',
                                                            'h1': 'Единицы площади'})


area_api = AreaApi()
area_api.router.include_router(cm2_api.router)
area_api.router.include_router(m2_api.router)
area_api.router.include_router(dm2_api.router)