from starlette.responses import HTMLResponse
from geometry import main_forms
from geometry.models import Circle
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from utils import get_similar_page


class CircleApi:

    def __init__(self):
        self.router = APIRouter(prefix='/circle', tags=['Circle'])
        self.templates = Jinja2Templates(directory="templates")
        self.figure: str = 'круга'
        self.context: dict = {}

        @self.router.get("/area/", response_class=HTMLResponse, name='circle_area')
        async def area(request: Request):
            similar_pages = await get_similar_page('Площадь')
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Найти площадь ' + self.figure,
                 'h1': 'Площадь ' + self.figure,
                 'h2': 'найти через радиус',
                 'h3': 'Площадь ' + self.figure + ' равна',
                 'action': 'circle_area_result',
                 'main_form': main_forms.circle,
                 "similar_pages": similar_pages},
                )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)

        @self.router.get("/area_result/", response_class=HTMLResponse, name='circle_area_result')
        async def area_result(request: Request, radius: float):
            circle = Circle(radius=radius)
            result = circle.get_area()
            self.context["result"] = result
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)

        @self.router.get("/len/", response_class=HTMLResponse, name='circle_len')
        async def len(request: Request):
            similar_pages = await get_similar_page('Длина')
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Найти длину ' + self.figure,
                 'h1': 'Длина ' + self.figure,
                 'h2': 'найти через радиус',
                 'h3': 'Длина ' + self.figure + ' равен',
                 'action': 'circle_len_result',
                 'main_form': main_forms.circle,
                 'similar_pages': similar_pages
                 })
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)

        @self.router.get("/circle_len_result/", response_class=HTMLResponse, name='circle_len_result')
        async def len_result(request: Request, radius: float):
            circle = Circle(radius=radius)
            result = circle.get_length()
            self.context["result"] = result
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)
