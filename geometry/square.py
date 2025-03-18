from starlette.responses import HTMLResponse
from geometry.models import Square
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

router = APIRouter(prefix='/square', tags=['Square'])
templates = Jinja2Templates(directory="templates")

FIGURE = 'квадрата'
H2 = 'найти через сторону'

context_diag = {
        'title': 'Найти диагональ ' + FIGURE,
        'h1': 'Диагональ ' + FIGURE,
        'h2': H2,
        'h3': 'Диагональ ' + FIGURE + ' равна',
        'action': 'square_diag_result'
    }

context_area = {
        'title': 'Найти площадь ' + FIGURE,
        'h1': 'Площадь ' + FIGURE,
        'h2': H2,
        'h3': 'Площадь ' + FIGURE + ' равна',
        'action': 'square_area_result'
    }

context_perimeter = {
        'title': 'Найти периметр ' + FIGURE,
        'h1': 'Периметр ' + FIGURE,
        'h2': H2,
        'h3': 'Периметр ' + FIGURE + ' равен',
        'action': 'square_len_result'
    }


@router.get("/area/", response_class=HTMLResponse, name='square_area')
def area(request: Request):

    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/square.html", context=context_area)


@router.get("/area_result/", response_class=HTMLResponse, name='square_area_result')
async def area_result(request: Request, a: float):
    new_square = Square(a=a)
    result = new_square.get_area()
    context_area['result'] = result
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/square.html", context=context_area)


@router.get("/len/", response_class=HTMLResponse, name='square_len')
def len(request: Request):
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/square.html", context=context_perimeter)


@router.get("/len_result/", response_class=HTMLResponse, name='square_len_result')
async def len_result(request: Request, a: float):
    new_square = Square(a=a)
    result = new_square.get_perimeter()
    context_perimeter['result'] = result
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/square.html", context=context_perimeter)


@router.get("/diag/", response_class=HTMLResponse, name='square_diag')
def diag(request: Request):
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/square.html", context=context_diag)


@router.get("/diag_result/", response_class=HTMLResponse, name='square_diag_result')
async def diag_result(request: Request, a: float):
    new_square = Square(a=a)
    result = new_square.get_diag()
    context_diag['result'] = result
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/square.html", context=context_diag)