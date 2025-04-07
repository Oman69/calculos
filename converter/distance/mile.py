from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from converter.distance import texts
from converter.distance.models import Mile


class MileApi:

    def __init__(self):
        self.router = APIRouter(prefix='/mile', tags=['Mile'])
        self.templates = Jinja2Templates(directory="templates")
        self.context: dict = {}
        self.name = 'Мили'

        @self.router.get("/result/", response_class=HTMLResponse, name='mile-result')
        async def result(request: Request, value: float, item_change: str):
            item = Mile(value=value, item_change=item_change)
            result = item.convert()
            self.context["result"] = result
            self.context["value"] = value
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)


class MileFunc:
    def __init__(self, api, change_name, link, main_text=None):
        self.api: MileApi = api
        self.router = APIRouter(prefix='/' + link, tags=[link])

        @api.router.get('/' + link + '/', response_class=HTMLResponse, name='ml_' + link)
        async def new_func(request: Request):
            self.api.context.pop('result', None)
            self.api.context.update(
                {'title': self.api.name + ' в ' + change_name + 'ы, сколько ' + change_name + 'ов в миле | ',
                 'h1': self.api.name + ' в ' + change_name + 'ы',
                 'h2': 'перевести',
                 'h3': 'Эквивалент ' + change_name + 'ов',
                 'action': 'mile-result',
                 'item_change': link,
                 'item_name': self.api.name,
                 "main_text": main_text},
            )
            # Получить данные
            return self.api.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.api.context)


ml_api = MileApi()
ml_api.router.include_router(MileFunc(api=ml_api, change_name='миллиметр', link='mm').router)
ml_api.router.include_router(MileFunc(api=ml_api, change_name='сантиметр', link='cm').router)
ml_api.router.include_router(MileFunc(api=ml_api, change_name='дециметр', link='dm').router)
ml_api.router.include_router(MileFunc(api=ml_api, change_name='метр', link='m').router)
ml_api.router.include_router(MileFunc(api=ml_api, change_name='километр', link='km').router)
ml_api.router.include_router(MileFunc(api=ml_api, change_name='дюйм', link='inch').router)
ml_api.router.include_router(MileFunc(api=ml_api, change_name='фут', link='ft').router)



