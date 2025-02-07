from models import Circle
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates

router = APIRouter(prefix='/geometry', tags=['Geometry'])
templates = Jinja2Templates(directory="templates")


@router.get("/circle_area/", response_class=HTMLResponse, name='circle_area')
def circle_area(request: Request):
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/circle_area.html", context={"id": 12}
    )


@router.get("/circle_area_result/", response_class=HTMLResponse, name='circle_area_result')
async def circle_area_result(request: Request, radius: str):
    circle = Circle(radius=radius)
    result = circle.get_area()
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/circle_area.html", context={"result": result}
    )


@router.get("/circle_len/", response_class=HTMLResponse, name='circle_len')
def circle_len(request: Request):
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/circle_len.html", context={"id": 12}
    )


@router.get("/circle_len_result/", response_class=HTMLResponse, name='circle_len_result')
async def circle_len_result(request: Request, radius: str):
    circle = Circle(radius=radius)
    result = circle.get_length()
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/circle_len.html", context={"result": result}
    )
