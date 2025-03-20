from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from geometry.models import Rhombus
from geometry import main_forms
from utils import get_similar_page


class RhombusApi:

    def __init__(self):
        self.router = APIRouter(prefix='/rhombus', tags=['Rhombus'])
        self.templates = Jinja2Templates(directory="templates")
        self.figure: str = 'ромба'
        self.context: dict = {}

        @self.router.get("/area/", response_class=HTMLResponse, name='rhombus_area')
        async def area(request: Request):
            similar_pages = await get_similar_page('Площадь')
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Найти площадь ' + self.figure,
                    'h1': 'Площадь ' + self.figure,
                    'h2': 'найти через сторону и высоту',
                    'h3': 'Площадь ' + self.figure + ' равна',
                    'action': 'rhombus_area_result',
                    'similar_pages': similar_pages,
                    'main_form': main_forms.rhombus_area})

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)

        @self.router.get("/area_result/", response_class=HTMLResponse, name='rhombus_area_result')
        def area_result(request: Request, a: float, h: float):
            new_rec = Rhombus(a=a, h=h)
            result = new_rec.get_area()
            self.context['result'] = result
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)

        @self.router.get("/perimeter/", response_class=HTMLResponse, name='rhombus_perimeter')
        async def perimeter(request: Request):
            similar_pages = await get_similar_page('Периметр')
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Найти периметр ' + self.figure,
                 'h1': 'Периметр ' + self.figure,
                 'h2': 'найти через сторону',
                 'h3': 'Периметр ' + self.figure + ' равен',
                 'action': 'rhombus_perimeter_result',
                 'similar_pages': similar_pages,
                 'main_form': main_forms.rhombus_perimeter})

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)

        @self.router.get("/perimeter_result/", response_class=HTMLResponse, name='rhombus_perimeter_result')
        async def perimeter_result( request: Request, a: float):
            new_rec = Rhombus(a=a)
            result = new_rec.get_perimeter()
            self.context['result'] = result
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)