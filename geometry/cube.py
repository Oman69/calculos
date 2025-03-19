from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from geometry.models import Cube

router = APIRouter(prefix='/cube', tags=['Cube'])
templates = Jinja2Templates(directory="templates")

FIGURE = 'куба'
H2 = 'найти через ребро'

context_area = {
        'title': 'Найти площадь ' + FIGURE,
        'h1': 'Площадь ' + FIGURE,
        'h2': H2,
        'h3': 'Площадь ' + FIGURE + ' равна',
        'action': 'cube_area_result'
    }

context_volume = {
        'title': 'Найти объем ' + FIGURE,
        'h1': 'Объем ' + FIGURE,
        'h2': H2,
        'h3': 'Объем ' + FIGURE + ' равен',
        'action': 'cube_volume_result'
    }


@router.get("/area/", response_class=HTMLResponse, name='cube_area')
def area(request: Request):

    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/cube.html", context=context_area)


@router.get("/area_result/", response_class=HTMLResponse, name='cube_area_result')
async def area_result(request: Request, a: float):
    new_cube = Cube(a=a)
    result = new_cube.get_area()
    context_area['result'] = result

    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/cube.html", context=context_area)


@router.get("/volume/", response_class=HTMLResponse, name='cube_volume')
def volume(request: Request):

    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/cube.html", context=context_volume)


@router.get("/volume_result/", response_class=HTMLResponse, name='cube_volume_result')
async def volume_result(request: Request, a: float):
    new_cube = Cube(a=a)
    result = new_cube.get_volume()
    context_volume['result'] = result
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/cube.html", context=context_volume)