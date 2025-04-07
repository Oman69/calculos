from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from converter.distance.models import Foot


class FootApi:

    def __init__(self):
        self.router = APIRouter(prefix='/foot', tags=['Foot'])
        self.templates = Jinja2Templates(directory="templates")
        self.context: dict = {}
        self.name = 'Футы'

        @self.router.get("/result/", response_class=HTMLResponse, name='foot-result')
        async def result(request: Request, value: float, item_change: str):
            item = Foot(value=value, item_change=item_change)
            result = item.convert()
            self.context["result"] = result
            self.context["value"] = value
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)


class FootFunc:
    def __init__(self, api, change_name, link, main_text=None):
        self.api: FootApi = api
        self.router = APIRouter(prefix='/' + link, tags=[link])

        @api.router.get('/' + link + '/', response_class=HTMLResponse, name='ft_' + link)
        async def new_func(request: Request):
            self.api.context.pop('result', None)
            self.api.context.update(
                {'title': 'Сколько ' + change_name + 'ов в футе | ',
                 'h1': self.api.name + ' в ' + change_name + 'ы',
                 'h2': 'перевести',
                 'h3': 'Эквивалент ' + change_name + 'ов',
                 'action': 'foot-result',
                 'item_change': link,
                 'item_name': self.api.name,
                 "main_text": main_text},
            )
            # Получить данные
            return self.api.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.api.context)


ft_api = FootApi()
ft_api.router.include_router(FootFunc(api=ft_api, change_name='миллиметр', link='mm').router)
ft_api.router.include_router(FootFunc(api=ft_api, change_name='сантиметр', link='cm').router)
ft_api.router.include_router(FootFunc(api=ft_api, change_name='дециметр', link='dm').router)
ft_api.router.include_router(FootFunc(api=ft_api, change_name='метр', link='m').router)
ft_api.router.include_router(FootFunc(api=ft_api, change_name='километр', link='km').router)
ft_api.router.include_router(FootFunc(api=ft_api, change_name='дюйм', link='inch').router)
ft_api.router.include_router(FootFunc(api=ft_api, change_name='ярд', link='ya').router)



