from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
import utils
from converter import main_forms
from converter.models import Gram


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

        @self.router.get("/gram-kilogram/", response_class=HTMLResponse, name='gram_kilogram')
        async def gram_kilogram(request: Request):

            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько грамм в килограмме',
                 'h1': 'Граммы в килограммы',
                 'h2': 'перевести',
                 'h3': 'Итого килограмм',
                 'from': 'Граммы',
                 'to': 'Килограммы',
                 'action': 'gram_kilogram_result',
                 'main_form': main_forms.gram,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/gram_kilogram_result/", response_class=HTMLResponse, name='gram_kilogram_result')
        async def gram_kilogram_result(request: Request, value: float):
            item = Gram(value=value)
            result = item.to_kilogram()
            self.context["result"] = result
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)

        @self.router.get("/kilogram-gram/", response_class=HTMLResponse, name='kilogram_gram')
        async def kilogram_gram(request: Request):

            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько килограмм в грамме',
                 'h1': 'Килограммы в граммы',
                 'h2': 'перевести',
                 'from': 'Граммы',
                 'to': 'Килограммы',
                 'action': 'gram_kilogram_result',
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)