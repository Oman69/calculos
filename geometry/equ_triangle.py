from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from geometry import main_forms, texts
from geometry.models import EquTriangle
from utils import get_similar_page


class EquTriangleApi:

    def __init__(self):
        self.router = APIRouter(prefix='/equ_triangle', tags=['EquTriangle'])
        self.templates = Jinja2Templates(directory="templates")
        self.figure = 'равностороннего треугольника'
        self.context = {'title': 'Найти площадь ' + self.figure,
                        'h1': 'Площадь ' + self.figure,
                        'h2': 'найти через сторону',
                        'h3': 'Площадь ' + self.figure + ' равна',
                        'action': 'equ_triangle_area_result',
                        'main_form': main_forms.equ_triangle,
                        'main_text': texts.equ_triangle_area}

        @self.router.get("/area/", response_class=HTMLResponse, name='equ_triangle_area')
        async def area(request: Request):
            similar_pages = await get_similar_page('Площадь')
            self.context.pop('result', None)
            self.context['similar_pages'] = similar_pages

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)

        @self.router.get("/area_result/", response_class=HTMLResponse, name='equ_triangle_area_result')
        async def area_result(request: Request, a: float):
            new_rec = EquTriangle(a=a)
            result = new_rec.get_area()
            self.context['result'] = result
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)

        @self.router.get("/height/", response_class=HTMLResponse, name='equ_triangle_height')
        async def height(request: Request):
            similar_pages = await get_similar_page('Высота')
            self.context.pop('result', None)

            self.context.update(
                {'title': 'Найти высоту ' + self.figure,
                 'h1': 'Высота ' + self.figure,
                 'h3': 'Высота ' + self.figure + ' равна',
                 'action': 'equ_triangle_height_result',
                 'similar_pages': similar_pages,
                 'main_form': main_forms.equ_triangle,
                 'main_text': texts.equ_triangle_height}
            )

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)

        @self.router.get("/height_result/", response_class=HTMLResponse, name='equ_triangle_height_result')
        async def height_result(request: Request, a: float):
            new_rec = EquTriangle(a=a)
            result = new_rec.get_height()
            self.context['result'] = result

            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)