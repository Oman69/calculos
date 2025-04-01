from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from converter.weight.models import Microgram


class MicrogramApi:

    def __init__(self):
        self.router = APIRouter(prefix='/microgram', tags=['Microgram'])
        self.templates = Jinja2Templates(directory="templates")
        self.context: dict = {}
        self.name = 'Микрограммы'

        @self.router.get("/result/", response_class=HTMLResponse, name='micro-result')
        async def result(request: Request, value: float, item_change: str):
            item = Microgram(value=value, item_change=item_change)
            result = item.convert()
            self.context["result"] = result
            self.context["value"] = value
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/g/", response_class=HTMLResponse, name='mkg_g')
        async def g(request: Request):

            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько грамм в микрограмме | ',
                 'h1': self.name + ' в граммы',
                 'h2': 'перевести',
                 'h3': 'Итого грамм',
                 'action': 'micro-result',
                 'item_change': 'g',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/kg/", response_class=HTMLResponse, name='mkg_kg')
        async def kg(request: Request):

            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько килограмм в микрограмме | ',
                 'h1': self.name + ' в килограммы',
                 'h2': 'перевести',
                 'h3': 'Итого килограмм',
                 'action': 'micro-result',
                 'item_change': 'kg',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/mg/", response_class=HTMLResponse, name='mkg_mg')
        async def mg(request: Request):

            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько милиграмм в микрограмме | ',
                 'h1': self.name + ' в милиграммы',
                 'h2': 'перевести',
                 'h3': 'Итого милиграмм',
                 'action': 'micro-result',
                 'item_change': 'mg',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/c/", response_class=HTMLResponse, name='mkg_c')
        async def c(request: Request):
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько центнеров в микрограмме | ',
                 'h1': self.name + ' в центнеры',
                 'h2': 'перевести',
                 'h3': 'Итого центнеров',
                 'action': 'micro-result',
                 'item_change': 'c',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/t/", response_class=HTMLResponse, name='mkg_t')
        async def t(request: Request):
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько тонн в микрограмме | ',
                 'h1': self.name + ' в тонны',
                 'h2': 'перевести',
                 'h3': 'Итого тонн',
                 'action': 'micro-result',
                 'item_change': 't',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/k/", response_class=HTMLResponse, name='mkg_k')
        async def k(request: Request):
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько карат в микрограмме | ',
                 'h1': self.name + ' в караты',
                 'h2': 'перевести',
                 'h3': 'Итого карат',
                 'action': 'micro-result',
                 'item_change': 'k',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)
