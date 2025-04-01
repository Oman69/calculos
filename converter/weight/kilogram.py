from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from converter.weight.models import Kilogram


class KilogramApi:

    def __init__(self):
        self.router = APIRouter(prefix='/kilogram', tags=['Kilogram'])
        self.templates = Jinja2Templates(directory="templates")
        self.context: dict = {}
        self.name = 'Килограммы'

        @self.router.get("/result/", response_class=HTMLResponse, name='kilo-result')
        async def result(request: Request, value: float, item_change: str):
            item = Kilogram(value=value, item_change=item_change)
            result = item.convert()
            self.context["result"] = result
            self.context["value"] = value
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/g/", response_class=HTMLResponse, name='kg_g')
        async def g(request: Request):

            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько грамм в килограмме | ',
                 'h1': self.name + ' в граммы',
                 'h2': 'перевести',
                 'h3': 'Итого грамм',
                 'action': 'kilo-result',
                 'item_change': 'g',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/mg/", response_class=HTMLResponse, name='kg_mg')
        async def mg(request: Request):

            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько милиграмм в килограмме | ',
                 'h1': self.name + ' в милиграммы',
                 'h2': 'перевести',
                 'h3': 'Итого милиграмм',
                 'action': 'kilo-result',
                 'item_change': 'mg',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/mkg/", response_class=HTMLResponse, name='kg_mkg')
        async def mkg(request: Request):

            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько микрограмм в килограмме | ',
                 'h1': self.name + ' в микрограммы',
                 'h2': 'перевести',
                 'h3': 'Итого микрограмм',
                 'action': 'kilo-result',
                 'item_change': 'mkg',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/c/", response_class=HTMLResponse, name='kg_c')
        async def c(request: Request):
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько центнеров в килограмме | ',
                 'h1': self.name + ' в центнеры',
                 'h2': 'перевести',
                 'h3': 'Итого центнеров',
                 'action': 'kilo-result',
                 'item_change': 'c',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/t/", response_class=HTMLResponse, name='kg_t')
        async def t(request: Request):
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько тонн в килограмме | ',
                 'h1': self.name + ' в тонны',
                 'h2': 'перевести',
                 'h3': 'Итого тонн',
                 'action': 'kilo-result',
                 'item_change': 't',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/k/", response_class=HTMLResponse, name='kg_k')
        async def k(request: Request):
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько карат в грамме | ',
                 'h1': self.name + ' в караты',
                 'h2': 'перевести',
                 'h3': 'Итого карат',
                 'action': 'kilo-result',
                 'item_change': 'k',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)
