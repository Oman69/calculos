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
            self.context["value"] = value
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/kg/", response_class=HTMLResponse, name='g_kg')
        async def kg(request: Request):

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

        @self.router.get("/mg/", response_class=HTMLResponse, name='g_mg')
        async def mg(request: Request):

            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько милиграмм в грамме | ',
                 'h1': self.name + ' в милиграммы',
                 'h2': 'перевести',
                 'h3': 'Итого милиграмм',
                 'action': 'gram-result',
                 'item_change': 'mg',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/mkg/", response_class=HTMLResponse, name='g_mkg')
        async def mkg(request: Request):

            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько микрограмм в грамме | ',
                 'h1': self.name + ' в микрограммы',
                 'h2': 'перевести',
                 'h3': 'Итого микрограмм',
                 'action': 'gram-result',
                 'item_change': 'mkg',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/c/", response_class=HTMLResponse, name='g_c')
        async def c(request: Request):
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько центнеров в грамме | ',
                 'h1': 'Граммы в центнеры',
                 'h2': 'перевести',
                 'h3': 'Итого центнеров',
                 'action': 'gram-result',
                 'item_change': 'c',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/t/", response_class=HTMLResponse, name='g_t')
        async def t(request: Request):
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько тонн в грамме | ',
                 'h1': 'Граммы в тонны',
                 'h2': 'перевести',
                 'h3': 'Итого тонн',
                 'action': 'gram-result',
                 'item_change': 't',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/k/", response_class=HTMLResponse, name='g_k')
        async def k(request: Request):
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько карат в грамме | ',
                 'h1': 'Граммы в караты',
                 'h2': 'перевести',
                 'h3': 'Итого карат',
                 'action': 'gram-result',
                 'item_change': 'k',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)
