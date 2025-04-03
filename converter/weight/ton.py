from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from converter.weight.models import Ton


class TonApi:

    def __init__(self):
        self.router = APIRouter(prefix='/ton', tags=['Ton'])
        self.templates = Jinja2Templates(directory="templates")
        self.context: dict = {}
        self.name = 'Тонны'

        @self.router.get("/result/", response_class=HTMLResponse, name='ton-result')
        async def result(request: Request, value: float, item_change: str):
            item = Ton(value=value, item_change=item_change)
            result = item.convert()
            self.context["result"] = result
            self.context["value"] = value
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/g/", response_class=HTMLResponse, name='t_g')
        async def g(request: Request):

            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько грамм в тонне | ',
                 'h1': self.name + ' в граммы',
                 'h2': 'перевести',
                 'h3': 'Итого грамм',
                 'action': 'ton-result',
                 'item_change': 'g',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/kg/", response_class=HTMLResponse, name='t_kg')
        async def kg(request: Request):

            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько килограмм в тонне | ',
                 'h1': self.name + ' в килограммы',
                 'h2': 'перевести',
                 'h3': 'Итого килограмм',
                 'action': 'ton-result',
                 'item_change': 'kg',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/mg/", response_class=HTMLResponse, name='t_mg')
        async def mg(request: Request):

            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько милиграмм в тонне | ',
                 'h1': self.name + ' в милиграммы',
                 'h2': 'перевести',
                 'h3': 'Итого милиграмм',
                 'action': 'ton-result',
                 'item_change': 'mg',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/c/", response_class=HTMLResponse, name='t_mkg')
        async def c(request: Request):
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько микрограмм в тонне | ',
                 'h1': self.name + ' в микрограммы',
                 'h2': 'перевести',
                 'h3': 'Итого микрограмм',
                 'action': 'ton-result',
                 'item_change': 'mkg',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/t/", response_class=HTMLResponse, name='t_c')
        async def t(request: Request):
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько центнеров в тонне | ',
                 'h1': self.name + ' в центнеры',
                 'h2': 'перевести',
                 'h3': 'Итого центнеров',
                 'action': 'ton-result',
                 'item_change': 'c',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/k/", response_class=HTMLResponse, name='t_k')
        async def k(request: Request):
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Сколько карат в тонне | ',
                 'h1': self.name + ' в караты',
                 'h2': 'перевести',
                 'h3': 'Итого карат',
                 'action': 'ton-result',
                 'item_change': 'k',
                 'item_name': self.name,
                 "main_text": ''},
            )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)
