from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from converter.distance.models import Inch


class InchApi:

    def __init__(self):
        self.router = APIRouter(prefix='/inch', tags=['Inch'])
        self.templates = Jinja2Templates(directory="templates")
        self.context: dict = {}
        self.name = 'Дюймы'

        @self.router.get("/result/", response_class=HTMLResponse, name='inch-result')
        async def result(request: Request, value: float, item_change: str):
            item = Inch(value=value, item_change=item_change)
            result = item.convert()
            self.context["result"] = result
            self.context["value"] = value
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)


class InchFunc:
    def __init__(self, api, change_name, link, main_text=None):
        self.api: InchApi = api
        self.router = APIRouter(prefix='/' + link, tags=[link])

        @api.router.get('/' + link + '/', response_class=HTMLResponse, name='inch_' + link)
        async def new_func(request: Request):
            self.api.context.pop('result', None)
            self.api.context.update(
                {'title': 'Сколько ' + change_name + 'ов в дюйме | ',
                 'h1': self.api.name + ' в ' + change_name + 'ы',
                 'h2': 'перевести',
                 'h3': 'Эквивалент ' + change_name + 'ов',
                 'action': 'inch-result',
                 'item_change': link,
                 'item_name': self.api.name,
                 "main_text": main_text},
            )
            # Получить данные
            return self.api.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.api.context)


inch_api = InchApi()
inch_api.router.include_router(InchFunc(api=inch_api, change_name='миллиметр', link='mm').router)
inch_api.router.include_router(InchFunc(api=inch_api, change_name='сантиметр', link='cm').router)
inch_api.router.include_router(InchFunc(api=inch_api, change_name='дециметр', link='dm').router)
inch_api.router.include_router(InchFunc(api=inch_api, change_name='метр', link='m').router)
inch_api.router.include_router(InchFunc(api=inch_api, change_name='километр', link='km').router)
inch_api.router.include_router(InchFunc(api=inch_api, change_name='фут', link='ft').router)
inch_api.router.include_router(InchFunc(api=inch_api, change_name='ярд', link='ya').router)



