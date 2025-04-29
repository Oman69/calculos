from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from geometry import main_forms, texts
from geometry.models import Trap
from utils import get_similar_page


class TrapApi:

    def __init__(self):
        self.router = APIRouter(prefix='/trap', tags=['Trap'])
        self.templates = Jinja2Templates(directory="templates")
        self.figure: str = 'трапеции'
        self.context: dict = {}

        @self.router.get("/area/", response_class=HTMLResponse, name='trap_area')
        async def area(request: Request):
            similar_pages = await get_similar_page('Площадь')
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Найти площадь ' + self.figure + ' | ',
                    'h1': 'Площадь ' + self.figure,
                    'h2': 'найти через основания и высоту',
                    'h3': 'Площадь ' + self.figure + ' равна',
                    'action': 'trap_area_result',
                    'similar_pages': similar_pages,
                    'main_form': main_forms.trap_area,
                    'main_text': texts.trap_area})
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)

        @self.router.get("/area_result/", response_class=HTMLResponse, name='trap_area_result')
        async def area_result(request: Request, a: float, b: float, h: float):
            new_trap = Trap(a=a, b=b, h=h)
            result = new_trap.get_area()
            self.context['result'] = result
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)

        @self.router.get("/perimeter/", response_class=HTMLResponse, name='trap_perimeter')
        async def perimeter(request: Request):
            similar_pages = await get_similar_page('Периметр')
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Найти периметр ' + self.figure + ' | ',
                 'h1': 'Периметр ' + self.figure,
                 'h2': 'найти через основания и стороны',
                 'h3': 'Периметр ' + self.figure + ' равен',
                 'action': 'trap_perimeter_result',
                 'similar_pages': similar_pages,
                 'main_form': main_forms.trap_perimeter,
                 'main_text': texts.trap_perimeter})
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)

        @self.router.get("/perimeter_result/", response_class=HTMLResponse, name='trap_perimeter_result')
        async def perimeter_result(request: Request, a: float, b: float, c: float, d: float):
            new_trap = Trap(a=a, b=b, c=c, d=d)
            result = new_trap.get_perimeter()
            self.context['result'] = result
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="geometry/base.html", context=self.context)
