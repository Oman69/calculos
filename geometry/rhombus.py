from fastapi.openapi.models import Schema
from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

from geometry.models import Rhombus

router = APIRouter(prefix='/rhombus', tags=['Rhombus'])
templates = Jinja2Templates(directory="templates")


class RhombusApi(Schema):

    figure: str = 'ромба'
    context: dict

    @router.get("/area/", response_class=HTMLResponse, name='rhombus_area')
    def area(self, request: Request):
        self.context.update(
            {'title': 'Найти площадь ' + self.figure,
                'h1': 'Площадь ' + self.figure,
                'h2': 'найти через сторону и высоту',
                'h3': 'Площадь ' + self.figure + ' равна',
                'action': 'rhombus_area_result',
                'main_form': """
                            <label class="form-label" for="a">Введите сторону <b>(A)</b></label>
                            <input type="number" class="form-control" id="a" name="a" step="any" required>
            
                            <label class="form-label" for="h">Введите высоту <b>(H)</b></label>
                            <input type="number" class="form-control" id="h" name="h" step="any" required>
                            """})

        # Получить данные
        return templates.TemplateResponse(
            request=request, name="geometry/base.html", context=self.context)

    @router.get("/area_result/", response_class=HTMLResponse, name='rhombus_area_result')
    async def area_result(self, request: Request, a: float, h: float):
        new_rec = Rhombus(a=a, h=h)
        result = new_rec.get_area()
        self.context['result'] = result
        # Получить данные
        return templates.TemplateResponse(
            request=request, name="geometry/base.html", context=self.context)

    @router.get("/perimeter/", response_class=HTMLResponse, name='rhombus_perimeter')
    def perimeter(self, request: Request):
        self.context.update(
            {'title': 'Найти периметр ' + self.figure,
             'h1': 'Периметр ' + self.figure,
             'h2': 'найти через сторону',
             'h3': 'Периметр ' + self.figure + ' равен',
             'action': 'rhombus_perimeter_result',
             'main_form': """<label class="form-label" for="a">Введите сторону <b>(A)</b></label>
                                <input type="number" class="form-control" id="a" name="a" step="any" required>"""
             })

        # Получить данные
        return templates.TemplateResponse(
            request=request, name="geometry/base.html", context=self.context)

    @router.get("/perimeter_result/", response_class=HTMLResponse, name='rhombus_perimeter_result')
    async def perimeter_result(self, request: Request, a: float):
        new_rec = Rhombus(a=a)
        result = new_rec.get_perimeter()
        self.context['result'] = result
        # Получить данные
        return templates.TemplateResponse(
            request=request, name="geometry/base.html", context=self.context)
