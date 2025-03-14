from pydantic import ValidationError
from sqlalchemy import select
from starlette.responses import HTMLResponse

from db_structure import pages, engine
from geometry.models import Circle
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

router = APIRouter(prefix='/circle', tags=['Circle'])
templates = Jinja2Templates(directory="templates")


async def get_similar_page(search_str: str):
    query = select(pages).where(pages.c.name.like(search_str + "%"))
    with engine.connect() as conn:
        data = [row for row in conn.execute(query)]
        return data


@router.get("/area/", response_class=HTMLResponse, name='circle_area')
async def area(request: Request):
    similar_pages = await get_similar_page('Площадь')
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/circle_area.html", context={"similar_pages": similar_pages}
    )


@router.get("/area_result/", response_class=HTMLResponse, name='circle_area_result')
async def area_result(request: Request, radius: float):
    similar_pages = await get_similar_page('Площадь')
    context = {"similar_pages": similar_pages}
    try:
        circle = Circle(radius=radius)
        result = circle.get_area()
        context["result"] = result
    except ValidationError:
        context["error"] = 'Значение поля не должно быть пустым!!!'
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/circle_area.html", context=context)


@router.get("/len/", response_class=HTMLResponse, name='circle_len')
async def len(request: Request):
    similar_pages = await get_similar_page('Длина')
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/circle_len.html", context={"similar_pages": similar_pages}
    )


@router.get("/circle_len_result/", response_class=HTMLResponse, name='circle_len_result')
async def len_result(request: Request, radius: float):
    similar_pages = await get_similar_page('Длина')
    circle = Circle(radius=radius)
    result = circle.get_length()
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/circle_len.html", context={"result": result, "similar_pages": similar_pages}
    )