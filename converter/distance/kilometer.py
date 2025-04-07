from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from converter.distance.models import Kilometer


class KilometerApi:

    def __init__(self):
        self.router = APIRouter(prefix='/kilometer', tags=['Kilometer'])
        self.templates = Jinja2Templates(directory="templates")
        self.context: dict = {}
        self.name = 'Километры'

        @self.router.get("/result/", response_class=HTMLResponse, name='kilometer-result')
        async def result(request: Request, value: float, item_change: str):
            item = Kilometer(value=value, item_change=item_change)
            result = item.convert()
            self.context["result"] = result
            self.context["value"] = value
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)


class KilometerFunc:
    def __init__(self, api, change_name, link, main_text=None):
        self.api: KilometerApi = api
        self.router = APIRouter(prefix='/' + link, tags=[link])

        @api.router.get('/' + link + '/', response_class=HTMLResponse, name='km_' + link)
        async def new_func(request: Request):
            self.api.context.pop('result', None)
            self.api.context.update(
                {'title': 'Сколько ' + change_name + 'ов в километре | ',
                 'h1': self.api.name + ' в ' + change_name + 'ы',
                 'h2': 'перевести',
                 'h3': 'Эквивалент ' + change_name + 'ов',
                 'action': 'kilometer-result',
                 'item_change': link,
                 'item_name': self.api.name,
                 "main_text": main_text},
            )
            # Получить данные
            return self.api.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.api.context)


km_api = KilometerApi()
km_api.router.include_router(KilometerFunc(api=km_api, change_name='миллиметр', link='mm').router)
km_api.router.include_router(KilometerFunc(api=km_api, change_name='сантиметр', link='cm').router)
km_api.router.include_router(KilometerFunc(api=km_api, change_name='дециметр', link='dm').router)
km_api.router.include_router(KilometerFunc(api=km_api, change_name='метр', link='m').router)
km_api.router.include_router(KilometerFunc(api=km_api, change_name='дюйм', link='inch').router)
km_api.router.include_router(KilometerFunc(api=km_api, change_name='фут', link='ft').router)
km_api.router.include_router(KilometerFunc(api=km_api, change_name='ярд', link='ya').router)



