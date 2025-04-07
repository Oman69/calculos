from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from converter.distance import texts
from converter.distance.models import Yard


class YardApi:

    def __init__(self):
        self.router = APIRouter(prefix='/yard', tags=['Yard'])
        self.templates = Jinja2Templates(directory="templates")
        self.context: dict = {}
        self.name = 'Ярды'

        @self.router.get("/result/", response_class=HTMLResponse, name='yard-result')
        async def result(request: Request, value: float, item_change: str):
            item = Yard(value=value, item_change=item_change)
            result = item.convert()
            self.context["result"] = result
            self.context["value"] = value
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)


class YardFunc:
    def __init__(self, api, change_name, link, main_text=None):
        self.api: YardApi = api
        self.router = APIRouter(prefix='/' + link, tags=[link])

        @api.router.get('/' + link + '/', response_class=HTMLResponse, name='ya_' + link)
        async def new_func(request: Request):
            self.api.context.pop('result', None)
            self.api.context.update(
                {'title': self.api.name + ' в ' + change_name + 'ы, сколько ' + change_name + 'ов в ярде | ',
                 'h1': self.api.name + ' в ' + change_name + 'ы',
                 'h2': 'перевести',
                 'h3': 'Эквивалент ' + change_name + 'ов',
                 'action': 'yard-result',
                 'item_change': link,
                 'item_name': self.api.name,
                 "main_text": main_text},
            )
            # Получить данные
            return self.api.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.api.context)


ya_api = YardApi()
ya_api.router.include_router(YardFunc(api=ya_api, change_name='миллиметр', link='mm').router)
ya_api.router.include_router(YardFunc(api=ya_api, change_name='сантиметр', link='cm').router)
ya_api.router.include_router(YardFunc(api=ya_api, change_name='дециметр', link='dm').router)
ya_api.router.include_router(YardFunc(api=ya_api, change_name='метр', link='m').router)
ya_api.router.include_router(YardFunc(api=ya_api, change_name='километр', link='km').router)
ya_api.router.include_router(YardFunc(api=ya_api, change_name='дюйм', link='inch').router)
ya_api.router.include_router(YardFunc(api=ya_api, change_name='фут', link='ft', main_text=texts.ya_ft).router)



