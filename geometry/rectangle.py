from starlette.responses import HTMLResponse
from geometry.models import Rectangle
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

router = APIRouter(prefix='/rectangle', tags=['Rectangle'])
templates = Jinja2Templates(directory="templates")


FIGURE = 'прямоугольника'
H2 = 'найти через стороны'

context_diag = {
        'title': 'Найти диагональ ' + FIGURE,
        'h1': 'Диагональ ' + FIGURE,
        'h2': H2,
        'h3': 'Диагональ ' + FIGURE + ' равна',
        'action': 'rectangle_diag_result'
    }

context_area = {
        'title': 'Найти площадь ' + FIGURE,
        'h1': 'Площадь ' + FIGURE,
        'h2': H2,
        'h3': 'Площадь ' + FIGURE + ' равна',
        'action': 'rectangle_area_result'
    }

context_perimeter = {
        'title': 'Найти периметр ' + FIGURE,
        'h1': 'Периметр ' + FIGURE,
        'h2': H2,
        'h3': 'Периметр ' + FIGURE + ' равен',
        'action': 'rectangle_len_result'
    }


@router.get("/area/", response_class=HTMLResponse, name='rectangle_area')
def area(request: Request):

    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/rectangle.html", context=context_area)


@router.get("/area_result/", response_class=HTMLResponse, name='rectangle_area_result')
async def area_result(request: Request, a: float, b: float):
    new_rec = Rectangle(a=a, b=b)
    result = new_rec.get_area()
    context_area['result'] = result
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/rectangle.html", context=context_area)


@router.get("/len/", response_class=HTMLResponse, name='rectangle_len')
def len(request: Request):
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/rectangle.html", context=context_perimeter)


@router.get("/len_result/", response_class=HTMLResponse, name='rectangle_len_result')
async def len_result(request: Request, a: float, b: float):
    new_rec = Rectangle(a=a, b=b)
    result = new_rec.get_perimeter()
    context_perimeter['result'] = result
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/rectangle.html", context=context_perimeter)


@router.get("/diag/", response_class=HTMLResponse, name='rectangle_diag')
def diag(request: Request):
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/rectangle.html", context=context_diag)


@router.get("/diag_result/", response_class=HTMLResponse, name='rectangle_diag_result')
async def diag_result(request: Request, a: float, b: float):
    new_square = Rectangle(a=a, b=b)
    result = new_square.get_diag()
    context_diag['result'] = result
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/rectangle.html", context=context_diag)