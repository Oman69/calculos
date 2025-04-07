import utils
from fastapi import APIRouter, Request
from converter.distance.meter import m_api
from converter.distance.foot import ft_api
from converter.distance.inch import inch_api
from starlette.responses import HTMLResponse
from converter.distance.decimeter import dm_api
from converter.distance.kilometer import km_api
from converter.distance.mile import ml_api
from converter.distance.millimeter import mm_api
from converter.distance.centimeter import cm_api
from starlette.templating import Jinja2Templates
from converter.distance.yard import ya_api


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
distance_api.router.include_router(m_api.router)
distance_api.router.include_router(km_api.router)
distance_api.router.include_router(inch_api.router)
distance_api.router.include_router(ft_api.router)
distance_api.router.include_router(ya_api.router)
distance_api.router.include_router(ml_api.router)