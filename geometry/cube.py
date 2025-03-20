from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from geometry import main_forms
from geometry.models import Cube
from utils import get_similar_page


class CubeApi:

    def __init__(self):
        self.router = APIRouter(prefix='/cube', tags=['Cube'])
        self.templates = Jinja2Templates(directory="templates")
        self.figure: str = 'куба'
        self.context: dict = {}

        @self.router.get("/area/", response_class=HTMLResponse, name='cube_area')
        async def area(request: Request):
            similar_pages = await get_similar_page('Площадь')
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Найти площадь ' + self.figure,
                    'h1': 'Площадь ' + self.figure,
                    'h2': 'найти через ребро',
                    'h3': 'Площадь ' + self.figure + ' равна',
                    'action': 'cube_area_result',
                    'similar_pages': similar_pages,
                    'main_form': main_forms.cube})

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)

        @self.router.get("/area_result/", response_class=HTMLResponse, name='cube_area_result')
        async def area_result(request: Request, a: float):
            new_cube = Cube(a=a)
            result = new_cube.get_area()
            self.context['result'] = result

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/cube.html", context=self.context)

        @self.router.get("/volume/", response_class=HTMLResponse, name='cube_volume')
        async def volume(request: Request):
            similar_pages = await get_similar_page('Объем')
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Найти объем ' + self.figure,
                 'h1': 'Объем ' + self.figure,
                 'h2': 'найти через ребро',
                 'h3': 'Объем ' + self.figure + ' равен',
                 'action': 'cube_volume_result',
                 'similar_pages': similar_pages,
                 'main_form': main_forms.cube
                 })

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)

        @self.router.get("/volume_result/", response_class=HTMLResponse, name='cube_volume_result')
        async def volume_result(request: Request, a: float):
            new_cube = Cube(a=a)
            result = new_cube.get_volume()
            self.context['result'] = result
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)