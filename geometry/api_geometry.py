from sqlalchemy import select
from db_structure import pages, engine
from models import Circle
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates

router = APIRouter(prefix='/geometry', tags=['Geometry'])
templates = Jinja2Templates(directory="templates")

@router.get("/circle_area/", response_class=HTMLResponse, name='circle_area')
def circle_area(request: Request):
    query = select(pages).where(pages.c.name.like("Площадь%"))
    with engine.connect() as conn:
        similar_pages = [row for row in conn.execute(query)]
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/circle_area.html", context={"similar_pages": similar_pages}
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


@router.get("/rectangle_area/", response_class=HTMLResponse, name='rectangle_area')
def rectangle_area(request: Request):

    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/circle_area.html", context={"similar_pages": 1}
    )


@router.get("/rectangle_area_result/", response_class=HTMLResponse, name='rectangle_area_result')
async def rectangle_area_result(request: Request, radius: str):
    circle = Circle(radius=radius)
    result = circle.get_area()
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/circle_area.html", context={"result": result}
    )


@router.get("/rectangle_len/", response_class=HTMLResponse, name='rectangle_len')
def rectangle_len(request: Request):
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/circle_len.html", context={"id": 12}
    )


@router.get("/rectangle_len_result/", response_class=HTMLResponse, name='rectangle_len_result')
async def rectangle_len_result(request: Request, radius: str):
    circle = Circle(radius=radius)
    result = circle.get_length()
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/circle_len.html", context={"result": result}
    )