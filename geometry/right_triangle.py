from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from geometry import main_forms, texts
from geometry.models import RightTriangle
from utils import get_similar_page


class RightTriangleApi:

    def __init__(self):
        self.router = APIRouter(prefix='/right_triangle', tags=['RightTriangle'])
        self.templates = Jinja2Templates(directory="templates")
        self.figure = 'прямоугольного треугольника'
        self.context = {'title': 'Найти площадь ' + self.figure,
                        'h1': 'Площадь ' + self.figure,
                        'h2': 'найти через катеты',
                        'h3': 'Площадь ' + self.figure + ' равна',
                        'action': 'right_triangle_area_result',
                        'main_form': main_forms.right_triangle,
                        'main_text': texts.right_triangle_area}

        @self.router.get("/area/", response_class=HTMLResponse, name='right_triangle_area')
        async def area(request: Request):
            similar_pages = await get_similar_page('Площадь')
            self.context.pop('result', None)
            self.context['similar_pages'] = similar_pages

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)

        @self.router.get("/area_result/", response_class=HTMLResponse, name='right_triangle_area_result')
        async def area_result(request: Request, a: float, b: float):
            new_rec = RightTriangle(a=a, b=b)
            result = new_rec.get_area()
            self.context['result'] = result
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)

        @self.router.get("/hypotenuse/", response_class=HTMLResponse, name='right_triangle_hypotenuse')
        async def hypotenuse(request: Request):
            similar_pages = await get_similar_page('Гипотенуза')
            self.context.pop('result', None)
            self.context['similar_pages'] = similar_pages

            self.context.update(
                {'title': 'Найти гипотенузу ' + self.figure,
                 'h1': 'Гипотенуза ' + self.figure,
                 'h2': 'найти через катеты',
                 'h3': 'Гипотенуза ' + self.figure + ' равна',
                 'action': 'right_triangle_hypotenuse_result',
                 'main_form': main_forms.right_triangle,
                 'main_text': texts.right_triangle_area}
            )

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)

        @self.router.get("/hypotenuse_result/", response_class=HTMLResponse, name='right_triangle_hypotenuse_result')
        async def hypotenuse_result(request: Request, a: float, b: float):
            new_rec = RightTriangle(a=a, b=b)
            result = new_rec.get_hypotenuse()
            self.context['result'] = result

            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)