from geometry import main_forms, texts
from utils import get_similar_page
from geometry.models import Rectangle
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from starlette.responses import HTMLResponse


class RectangleApi:

    def __init__(self):
        self.router = APIRouter(prefix='/rectangle', tags=['Rectangle'])
        self.templates = Jinja2Templates(directory="templates")
        self.figure: str = 'прямоугольника'
        self.context: dict = {}

        @self.router.get("/area/", response_class=HTMLResponse, name='rectangle_area')
        async def area(request: Request):
            similar_pages = await get_similar_page('Площадь')
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Найти площадь ' + self.figure,
                    'h1': 'Площадь ' + self.figure,
                    'h2': 'найти через стороны',
                    'h3': 'Площадь ' + self.figure + ' равна',
                    'action': 'rectangle_area_result',
                    'similar_pages': similar_pages,
                    'main_form': main_forms.rectangle,
                    'main_text': texts.rectangle_area})

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)

        @self.router.get("/area_result/", response_class=HTMLResponse, name='rectangle_area_result')
        async def area_result(request: Request, a: float, b: float):
            new_rec = Rectangle(a=a, b=b)
            result = new_rec.get_area()
            self.context['result'] = result

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)

        @self.router.get("/len/", response_class=HTMLResponse, name='rectangle_len')
        async def len(request: Request):
            similar_pages = await get_similar_page('Периметр')
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Найти периметр ' + self.figure,
                 'h1': 'Периметр ' + self.figure,
                 'h2': 'найти через стороны',
                 'h3': 'Периметр ' + self.figure + ' равен',
                 'action': 'rectangle_len_result',
                 'similar_pages': similar_pages,
                 'main_form': main_forms.rectangle,
                 'main_text': texts.rectangle_perimeter
                 })

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)

        @self.router.get("/len_result/", response_class=HTMLResponse, name='rectangle_len_result')
        async def len_result(request: Request, a: float, b: float):
            new_rec = Rectangle(a=a, b=b)
            result = new_rec.get_perimeter()
            self.context['result'] = result
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)

        @self.router.get("/diag/", response_class=HTMLResponse, name='rectangle_diag')
        async def diag(request: Request):
            similar_pages = await get_similar_page('Диагональ')
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Найти диагональ ' + self.figure,
                 'h1': 'Диагональ ' + self.figure,
                 'h2': 'найти через стороны',
                 'h3': 'Диагональ ' + self.figure + ' равна',
                 'action': 'rectangle_diag_result',
                 'similar_pages': similar_pages,
                 'main_form': main_forms.rectangle
                 })

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)

        @self.router.get("/diag_result/", response_class=HTMLResponse, name='rectangle_diag_result')
        async def diag_result(request: Request, a: float, b: float):
            new_square = Rectangle(a=a, b=b)
            result = new_square.get_diag()
            self.context['result'] = result
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)