from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from converter.weight.models import Centner


class CentnerApi:

    def __init__(self):
        self.router = APIRouter(prefix='/centner', tags=['Centner'])
        self.templates = Jinja2Templates(directory="templates")
        self.context: dict = {}
        self.name = 'Центнеры'

        @self.router.get("/result/", response_class=HTMLResponse, name='centner-result')
        async def result(request: Request, value: float, item_change: str):
            item = Centner(value=value, item_change=item_change)
            result = item.convert()
            self.context["result"] = result
            self.context["value"] = value
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/g/", response_class=HTMLResponse, name='c_g')
        async def g(request: Request):

            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько грамм в центнере | ',
                 'h1': self.name + ' в граммы',
                 'h2': 'перевести',
                 'h3': 'Итого грамм',
                 'action': 'centner-result',
                 'item_change': 'g',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/kg/", response_class=HTMLResponse, name='c_kg')
        async def kg(request: Request):

            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько килограмм в центнере | ',
                 'h1': self.name + ' в килограммы',
                 'h2': 'перевести',
                 'h3': 'Итого килограмм',
                 'action': 'centner-result',
                 'item_change': 'kg',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/mg/", response_class=HTMLResponse, name='c_mg')
        async def mg(request: Request):

            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько милиграмм в центнере | ',
                 'h1': self.name + ' в центнере',
                 'h2': 'перевести',
                 'h3': 'Итого милиграмм',
                 'action': 'centner-result',
                 'item_change': 'mg',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/c/", response_class=HTMLResponse, name='c_mkg')
        async def c(request: Request):
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько микрограмм в центнере | ',
                 'h1': self.name + ' в микрограммы',
                 'h2': 'перевести',
                 'h3': 'Итого микрограмм',
                 'action': 'centner-result',
                 'item_change': 'mkg',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/t/", response_class=HTMLResponse, name='c_t')
        async def t(request: Request):
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько тонн в центнере | ',
                 'h1': self.name + ' в тонны',
                 'h2': 'перевести',
                 'h3': 'Итого тонн',
                 'action': 'centner-result',
                 'item_change': 't',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/k/", response_class=HTMLResponse, name='c_k')
        async def k(request: Request):
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько карат в центнере | ',
                 'h1': self.name + ' в караты',
                 'h2': 'перевести',
                 'h3': 'Итого карат',
                 'action': 'centner-result',
                 'item_change': 'k',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)
