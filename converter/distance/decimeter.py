from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from converter.distance.models import Decimeter


class DecimeterApi:

    def __init__(self):
        self.router = APIRouter(prefix='/decimeter', tags=['Decimeter'])
        self.templates = Jinja2Templates(directory="templates")
        self.context: dict = {}
        self.name = 'Дециметры'

        @self.router.get("/result/", response_class=HTMLResponse, name='decimeter-result')
        async def result(request: Request, value: float, item_change: str):
            item = Decimeter(value=value, item_change=item_change)
            result = item.convert()
            self.context["result"] = result
            self.context["value"] = value
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)


class DecimeterFunc:
    def __init__(self, api, change_name, link, main_text=None):
        self.api: DecimeterApi = api
        self.router = APIRouter(prefix='/' + link, tags=[link])

        @api.router.get('/' + link + '/', response_class=HTMLResponse, name='dm_' + link)
        async def new_func(request: Request):
            self.api.context.pop('result', None)
            self.api.context.update(
                {'title': 'Сколько ' + change_name + 'ов в дециметре | ',
                 'h1': self.api.name + ' в ' + change_name + 'ы',
                 'h2': 'перевести',
                 'h3': 'Эквивалент ' + change_name + 'ов',
                 'action': 'decimeter-result',
                 'item_change': link,
                 'item_name': self.api.name,
                 "main_text": main_text},
            )
            # Получить данные
            return self.api.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.api.context)


dm_api = DecimeterApi()
dm_api.router.include_router(DecimeterFunc(api=dm_api, change_name='миллиметр', link='mm').router)
dm_api.router.include_router(DecimeterFunc(api=dm_api, change_name='сантиметр', link='cm').router)
dm_api.router.include_router(DecimeterFunc(api=dm_api, change_name='метр', link='m').router)
dm_api.router.include_router(DecimeterFunc(api=dm_api, change_name='километр', link='km').router)
dm_api.router.include_router(DecimeterFunc(api=dm_api, change_name='дюйм', link='inch').router)
dm_api.router.include_router(DecimeterFunc(api=dm_api, change_name='фут', link='ft').router)



