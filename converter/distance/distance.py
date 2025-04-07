from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
import utils
from converter.distance.millimeter import mm_api
from converter.distance.centimeter import cm_api
from converter.distance.decimeter import dm_api


class DistanceApi:

    def __init__(self):
        self.router = APIRouter(prefix='/distance', tags=['Distance'])
        self.templates = Jinja2Templates(directory="templates")
        self.context: dict = {}

        @self.router.get("", response_class=HTMLResponse, name='distance')
        async def distance(request: Request, limit: int = 6):

            filter_pages = utils.select_main_pages_by_category(32, limit)

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="home.html", context={'links': filter_pages,
                                                            'title': 'Расстояние и длина | ',
                                                            'h1': 'Расстояние и длина'})


distance_api = DistanceApi()
distance_api.router.include_router(mm_api.router)
distance_api.router.include_router(cm_api.router)
distance_api.router.include_router(dm_api.router)