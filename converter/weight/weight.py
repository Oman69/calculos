from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
import utils
from converter.weight.centner import CentnerApi
from converter.weight.gram import GramApi
from converter.weight.kilogram import KilogramApi
from converter.weight.microgram import MicrogramApi
from converter.weight.miligram import MilligramApi


class WeightApi:

    def __init__(self):
        self.router = APIRouter(prefix='/weight', tags=['Weight'])
        self.templates = Jinja2Templates(directory="templates")
        self.context: dict = {}

        @self.router.get("", response_class=HTMLResponse, name='weight')
        async def weight(request: Request, limit: int = 6):

            filter_pages = utils.select_main_pages_by_category(31, limit)

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="home.html", context={'links': filter_pages,
                                                            'title': 'Вес и масса | ',
                                                            'h1': 'Вес и масса'})


weight_api = WeightApi()
weight_api.router.include_router(GramApi().router)
weight_api.router.include_router(KilogramApi().router)
weight_api.router.include_router(MilligramApi().router)
weight_api.router.include_router(MicrogramApi().router)
weight_api.router.include_router(CentnerApi().router)