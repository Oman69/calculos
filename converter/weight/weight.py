from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
import utils
from converter.weight import main_forms
from converter.weight.gram import GramApi
from converter.weight.models import Gram, Kilogram


class WeightApi:

    def __init__(self):
        self.router = APIRouter(prefix='/weight', tags=['Weight'])
        self.templates = Jinja2Templates(directory="templates")
        self.context: dict = {}

        @self.router.get("", response_class=HTMLResponse, name='weight')
        async def weight(request: Request):

            filter_pages = utils.select_main_pages_by_category(31)

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="home.html", context={'links': filter_pages,
                                                            'title': 'Вес и масса | ',
                                                            'h1': 'Вес и масса'})

        @self.router.get("/kilogram-gram/", response_class=HTMLResponse, name='kilogram_gram')
        async def kilogram_gram(request: Request):

            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько килограмм в грамме',
                 'h1': 'Килограммы в граммы',
                 'h2': 'перевести',
                 'h3': 'Итого грамм',
                 'action': 'kilogram_gram_result',
                 'main_form': main_forms.kilogram,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/kilogram-gram-result/", response_class=HTMLResponse, name='kilogram_gram_result')
        async def kilogram_gram_result(request: Request, value: float):
            item = Kilogram(value=value)
            result = item.to_gram()
            self.context["result"] = result
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)


weight_api = WeightApi()
weight_api.router.include_router(GramApi().router)