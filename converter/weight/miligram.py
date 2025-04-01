from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from converter.weight.models import Milligram


class MilligramApi:

    def __init__(self):
        self.router = APIRouter(prefix='/milligram', tags=['Milligram'])
        self.templates = Jinja2Templates(directory="templates")
        self.context: dict = {}
        self.name = 'Милиграммы'

        @self.router.get("/result/", response_class=HTMLResponse, name='milli-result')
        async def result(request: Request, value: float, item_change: str):
            item = Milligram(value=value, item_change=item_change)
            result = item.convert()
            self.context["result"] = result
            self.context["value"] = value
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/g/", response_class=HTMLResponse, name='mg_g')
        async def g(request: Request):

            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько грамм в милиграмме | ',
                 'h1': self.name + ' в граммы',
                 'h2': 'перевести',
                 'h3': 'Итого грамм',
                 'action': 'milli-result',
                 'item_change': 'g',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/kg/", response_class=HTMLResponse, name='mg_kg')
        async def kg(request: Request):

            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько килограмм в милиграмме | ',
                 'h1': self.name + ' в килограммы',
                 'h2': 'перевести',
                 'h3': 'Итого килограмм',
                 'action': 'milli-result',
                 'item_change': 'kg',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/mkg/", response_class=HTMLResponse, name='mg_mkg')
        async def mkg(request: Request):

            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько микрограмм в милиграмме | ',
                 'h1': self.name + ' в микрограммы',
                 'h2': 'перевести',
                 'h3': 'Итого микрограмм',
                 'action': 'milli-result',
                 'item_change': 'mkg',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/c/", response_class=HTMLResponse, name='mg_c')
        async def c(request: Request):
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько центнеров в милиграмме | ',
                 'h1': self.name + ' в центнеры',
                 'h2': 'перевести',
                 'h3': 'Итого центнеров',
                 'action': 'milli-result',
                 'item_change': 'c',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/t/", response_class=HTMLResponse, name='mg_t')
        async def t(request: Request):
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько тонн в милиграмме | ',
                 'h1': self.name + ' в тонны',
                 'h2': 'перевести',
                 'h3': 'Итого тонн',
                 'action': 'milli-result',
                 'item_change': 't',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/k/", response_class=HTMLResponse, name='mg_k')
        async def k(request: Request):
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько карат в милиграмме | ',
                 'h1': self.name + ' в караты',
                 'h2': 'перевести',
                 'h3': 'Итого карат',
                 'action': 'milli-result',
                 'item_change': 'k',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)
