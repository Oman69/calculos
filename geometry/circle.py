from pydantic import ValidationError
from sqlalchemy import select
from starlette.responses import HTMLResponse

from db_structure import pages, engine
from geometry.models import Circle
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

router = APIRouter(prefix='/circle', tags=['Circle'])
templates = Jinja2Templates(directory="templates")


FIGURE = 'круга'
H2 = 'найти через радиус'


context_area = {
        'title': 'Найти площадь ' + FIGURE,
        'h1': 'Площадь ' + FIGURE,
        'h2': H2,
        'h3': 'Площадь ' + FIGURE + ' равна',
        'action': 'circle_area_result'
    }

context_perimeter = {
        'title': 'Найти длину окружности',
        'h1': 'Длина окружности',
        'h2': H2,
        'h3': 'Длина окружности равна',
        'action': 'circle_len_result'
    }


async def get_similar_page(search_str: str):
    query = select(pages).where(pages.c.name.like(search_str + "%"))
    with engine.connect() as conn:
        data = [row for row in conn.execute(query)]
        return data


@router.get("/area/", response_class=HTMLResponse, name='circle_area')
async def area(request: Request):
    similar_pages = await get_similar_page('Площадь')
    context_area["similar_pages"] = similar_pages
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/circle.html", context=context_area)


@router.get("/area_result/", response_class=HTMLResponse, name='circle_area_result')
async def area_result(request: Request, radius: float):
    try:
        circle = Circle(radius=radius)
        result = circle.get_area()
        context_area["result"] = result
    except ValidationError:
        context_area["error"] = 'Значение поля не должно быть пустым!!!'
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/circle.html", context=context_area)


@router.get("/len/", response_class=HTMLResponse, name='circle_len')
async def len(request: Request):
    similar_pages = await get_similar_page('Длина')
    context_perimeter["similar_pages"] = similar_pages
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/circle.html", context=context_perimeter)


@router.get("/circle_len_result/", response_class=HTMLResponse, name='circle_len_result')
async def len_result(request: Request, radius: float):
    circle = Circle(radius=radius)
    result = circle.get_length()
    context_perimeter["result"] = result
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/circle.html", context=context_perimeter)