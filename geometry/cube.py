from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from geometry.models import Cube

router = APIRouter(prefix='/cube', tags=['Cube'])
templates = Jinja2Templates(directory="templates")


@router.get("/area/", response_class=HTMLResponse, name='cube_area')
def area(request: Request):

    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/cube_area.html", context={"similar_pages": []}
    )


@router.get("/area_result/", response_class=HTMLResponse, name='cube_area_result')
async def area_result(request: Request, a: float):
    new_cube = Cube(a=a)
    result = new_cube.get_area()
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/cube_area.html", context={"result": result}
    )


@router.get("/volume/", response_class=HTMLResponse, name='cube_volume')
def volume(request: Request):

    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/cube_vol.html", context={"similar_pages": []}
    )


@router.get("/volume_result/", response_class=HTMLResponse, name='cube_volume_result')
async def volume_result(request: Request, a: float):
    new_cube = Cube(a=a)
    result = new_cube.get_volume()
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/cube_vol.html", context={"result": result}
    )