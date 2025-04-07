from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from converter.distance.models import Centimeter


class CentimeterApi:

    def __init__(self):
        self.router = APIRouter(prefix='/centimeter', tags=['Centimeter'])
        self.templates = Jinja2Templates(directory="templates")
        self.context: dict = {}
        self.name = 'Сантиметры'

        @self.router.get("/result/", response_class=HTMLResponse, name='centimeter-result')
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

        @api.router.get('/' + link + '/', response_class=HTMLResponse, name='cm_' + link)
        async def new_func(request: Request):
            self.api.context.pop('result', None)
            self.api.context.update(
                {'title': 'Сколько ' + change_name + 'ов в сантиметре | ',
                 'h1': 'Сантиметры в ' + change_name + 'ы',
                 'h2': 'перевести',
                 'h3': 'Эквивалент ' + change_name + 'ов',
                 'action': 'centimeter-result',
                 'item_change': link,
                 'item_name': 'Сантиметры',
                 "main_text": main_text},
            )
            # Получить данные
            return self.api.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.api.context)


cm_api = CentimeterApi()
cm_api.router.include_router(CentimeterFunc(api=cm_api, change_name='миллиметр', link='mm').router)
cm_api.router.include_router(CentimeterFunc(api=cm_api, change_name='дециметр', link='dm').router)
cm_api.router.include_router(CentimeterFunc(api=cm_api, change_name='метр', link='m').router)
cm_api.router.include_router(CentimeterFunc(api=cm_api, change_name='километр', link='km').router)
cm_api.router.include_router(CentimeterFunc(api=cm_api, change_name='дюйм', link='inch').router)
cm_api.router.include_router(CentimeterFunc(api=cm_api, change_name='фут', link='ft').router)
cm_api.router.include_router(CentimeterFunc(api=cm_api, change_name='ярд', link='ya').router)



