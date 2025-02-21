from sqlalchemy import select
from starlette.responses import HTMLResponse

from db_structure import pages, engine
from geometry.models import Circle
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

router = APIRouter(prefix='/circle', tags=['Circle'])
templates = Jinja2Templates(directory="templates")


@router.get("/area/", response_class=HTMLResponse, name='circle_area')
def area(request: Request):
    query = select(pages).where(pages.c.name.like("Площадь%"))
    with engine.connect() as conn:
        similar_pages = [row for row in conn.execute(query)]
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/circle_area.html", context={"similar_pages": similar_pages}
    )


@router.get("/area_result/", response_class=HTMLResponse, name='circle_area_result')
async def area_result(request: Request, radius: str):
    circle = Circle(radius=radius)
    result = circle.get_area()
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/circle_area.html", context={"result": result}
    )


@router.get("/len/", response_class=HTMLResponse, name='circle_len')
def len(request: Request):
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/circle_len.html", context={"id": 12}
    )


@router.get("/circle_len_result/", response_class=HTMLResponse, name='circle_len_result')
async def len_result(request: Request, radius: str):
    circle = Circle(radius=radius)
    result = circle.get_length()
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/circle_len.html", context={"result": result}
    )