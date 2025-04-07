from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from converter.distance.models import Millimeter


class MillimeterApi:

    def __init__(self):
        self.router = APIRouter(prefix='/millimeter', tags=['Millimeter'])
        self.templates = Jinja2Templates(directory="templates")
        self.context: dict = {}
        self.name = 'Миллиметры'

        @self.router.get("/result/", response_class=HTMLResponse, name='millimeter-result')
        async def result(request: Request, value: float, item_change: str):
            item = Millimeter(value=value, item_change=item_change)
            result = item.convert()
            self.context["result"] = result
            self.context["value"] = value
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)


class MillimeterFunc:
    def __init__(self, api, change_name, link, main_text=None):
        self.api: MillimeterApi = api
        self.router = APIRouter(prefix='/' + link, tags=[link])

        @api.router.get('/' + link + '/', response_class=HTMLResponse, name='mm_' + link)
        async def new_func(request: Request):
            self.api.context.pop('result', None)
            self.api.context.update(
                {'title': 'Сколько ' + change_name + 'ов в миллиметре | ',
                 'h1': 'Миллиметры в ' + change_name + 'ы',
                 'h2': 'перевести',
                 'h3': 'Эквивалент ' + change_name + 'ов',
                 'action': 'millimeter-result',
                 'item_change': link,
                 'item_name': 'Миллиметры',
                 "main_text": main_text},
            )
            # Получить данные
            return self.api.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.api.context)


mm_api = MillimeterApi()
mm_api.router.include_router(MillimeterFunc(api=mm_api, change_name='сантиметр', link='cm').router)
mm_api.router.include_router(MillimeterFunc(api=mm_api, change_name='дециметр', link='dm').router)
mm_api.router.include_router(MillimeterFunc(api=mm_api, change_name='метр', link='m').router)
mm_api.router.include_router(MillimeterFunc(api=mm_api, change_name='километр', link='km').router)
mm_api.router.include_router(MillimeterFunc(api=mm_api, change_name='дюйм', link='inch', main_text='Главный текст').router)
mm_api.router.include_router(MillimeterFunc(api=mm_api, change_name='фут', link='ft').router)



