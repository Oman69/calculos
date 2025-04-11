from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from converter.area.models import Centimeter


class CentimeterApi:

    def __init__(self):
        self.router = APIRouter(prefix='/cm2', tags=['Centimeter'])
        self.templates = Jinja2Templates(directory="templates")
        self.context: dict = {}
        self.name = 'Сантиметры²'

        @self.router.get("/result/", response_class=HTMLResponse, name='cm-result')
        async def result(request: Request, value: float, item_change: str):
            item = Centimeter(value=value, item_change=item_change)
            result = item.convert()
            self.context["result"] = result
            self.context["value"] = value
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)


class CentimeterFunc:
    def __init__(self, api, change_name, link, main_text=None):
        self.api: CentimeterApi = api
        self.router = APIRouter(prefix='/' + link, tags=[link])

        @api.router.get('/' + link + '/', response_class=HTMLResponse, name='cm2_' + link)
        async def new_func(request: Request):
            self.api.context.pop('result', None)
            self.api.context.update(
                {'title': 'Сколько квадратных ' + change_name + 'ов в квадратном сантиметре | ',
                 'h1': self.api.name + ' в ' + change_name + 'ы²',
                 'h2': 'перевести',
                 'h3': 'Эквивалент ' + change_name + 'ов²',
                 'action': 'cm-result',
                 'item_change': link,
                 'item_name': self.api.name,
                 "main_text": main_text},
            )
            # Получить данные
            return self.api.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.api.context)


cm2_api = CentimeterApi()
cm2_api.router.include_router(CentimeterFunc(api=cm2_api, change_name='дециметр', link='dm2').router)
cm2_api.router.include_router(CentimeterFunc(api=cm2_api, change_name='метр', link='m2').router)
cm2_api.router.include_router(CentimeterFunc(api=cm2_api, change_name='километр', link='km2').router)
cm2_api.router.include_router(CentimeterFunc(api=cm2_api, change_name='дюйм', link='inch2').router)
cm2_api.router.include_router(CentimeterFunc(api=cm2_api, change_name='фут', link='ft2').router)
cm2_api.router.include_router(CentimeterFunc(api=cm2_api, change_name='акр', link='akr2').router)
cm2_api.router.include_router(CentimeterFunc(api=cm2_api, change_name='гектар', link='ga2').router)



