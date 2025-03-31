from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from converter.weight.models import Gram


class GramApi:

    def __init__(self):
        self.router = APIRouter(prefix='/gram', tags=['Gram'])
        self.templates = Jinja2Templates(directory="templates")
        self.context: dict = {}
        self.name = 'Граммы'

        @self.router.get("/result/", response_class=HTMLResponse, name='gram-result')
        async def result(request: Request, value: float, item_change: str):
            item = Gram(value=value, item_change=item_change)
            result = item.convert()
            self.context["result"] = result
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/g-kg/", response_class=HTMLResponse, name='g_kg')
        async def g_kg(request: Request):

            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько килограмм в грамме | ',
                 'h1': self.name + ' в килограммы',
                 'h2': 'перевести',
                 'h3': 'Итого килограмм',
                 'action': 'gram-result',
                 'item_change': 'kg',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/g-mg/", response_class=HTMLResponse, name='g_mg')
        async def g_mg(request: Request):

            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько милиграмм в грамме | ',
                 'h1': self.name + ' в милиграммы',
                 'h3': 'Итого милиграмм',
                 'item_change': 'mg',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/g-mkg/", response_class=HTMLResponse, name='g_mkg')
        async def g_mkg(request: Request):

            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько микрограмм в грамме | ',
                 'h1': self.name + ' в микрограммы',
                 'h3': 'Итого микрограмм',
                 'item_change': 'mkg',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/g-c/", response_class=HTMLResponse, name='g_c')
        async def g_c(request: Request):
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько центнеров в грамме | ',
                 'h1': 'Граммы в центнеры',
                 'h3': 'Итого центнеров',
                 'item_change': 'c',
                 'item_name': self.name,
                 'action': 'gram-result',
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)
