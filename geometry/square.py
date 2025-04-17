from starlette.responses import HTMLResponse
from geometry import main_forms, texts
from geometry.models import Square
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from utils import get_similar_page


class SquareApi:

    def __init__(self):
        self.router = APIRouter(prefix='/square', tags=['Square'])
        self.templates = Jinja2Templates(directory="templates")
        self.figure: str = 'квадрата'
        self.context: dict = {}

        @self.router.get("/area/", response_class=HTMLResponse, name='square_area')
        async def area(request: Request):
            similar_pages = await get_similar_page('Площадь')
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Найти площадь ' + self.figure + ' | ',
                    'h1': 'Площадь ' + self.figure,
                    'h2': 'найти через сторону',
                    'h3': 'Площадь ' + self.figure + ' равна',
                    'action': 'square_area_result',
                    'similar_pages': similar_pages,
                    'main_form': main_forms.square,
                    'main_text': texts.square_area})

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)

        @self.router.get("/area_result/", response_class=HTMLResponse, name='square_area_result')
        async def area_result(request: Request, a: float):
            new_square = Square(a=a)
            result = new_square.get_area()
            self.context['result'] = result

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)

        @self.router.get("/len/", response_class=HTMLResponse, name='square_len')
        async def len(request: Request):
            similar_pages = await get_similar_page('Периметр')
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Найти периметр ' + self.figure + ' | ',
                 'h1': 'Периметр ' + self.figure,
                 'h2': 'найти через сторону',
                 'h3': 'Периметр ' + self.figure + ' равен',
                 'action': 'square_len_result',
                 'similar_pages': similar_pages,
                 'main_form': main_forms.square,
                 'main_text': texts.square_perimeter
                 })

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)

        @self.router.get("/len_result/", response_class=HTMLResponse, name='square_len_result')
        async def len_result(request: Request, a: float):
            new_square = Square(a=a)
            result = new_square.get_perimeter()
            self.context['result'] = result
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)

        @self.router.get("/diag/", response_class=HTMLResponse, name='square_diag')
        async def diag(request: Request):
            similar_pages = await get_similar_page('Диагональ')
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Найти периметр ' + self.figure + ' | ',
                 'h1': 'Диагональ ' + self.figure,
                 'h2': 'найти через сторону',
                 'h3': 'Диагональ ' + self.figure + ' равен',
                 'action': 'square_diag_result',
                 'similar_pages': similar_pages,
                 'main_form': main_forms.square,
                 'main_text': texts.square_diag

                 })

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)

        @self.router.get("/diag_result/", response_class=HTMLResponse, name='square_diag_result')
        async def diag_result(request: Request, a: float):
            new_square = Square(a=a)
            result = new_square.get_diag()
            self.context['result'] = result
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)