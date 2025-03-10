from starlette.responses import HTMLResponse
from geometry.models import Rectangle
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

router = APIRouter(prefix='/rectangle', tags=['Rectangle'])
templates = Jinja2Templates(directory="templates")


@router.get("/area/", response_class=HTMLResponse, name='rectangle_area')
def area(request: Request):

    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/rectangle_area.html", context={"similar_pages": []}
    )


@router.get("/area_result/", response_class=HTMLResponse, name='rectangle_area_result')
async def area_result(request: Request, a: str, b: str):
    new_rec = Rectangle(a=a, b=b)
    result = new_rec.get_area()
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/rectangle_area.html", context={"result": result}
    )


@router.get("/len/", response_class=HTMLResponse, name='rectangle_len')
def len(request: Request):
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/rectangle_len.html", context={"id": 12}
    )


@router.get("/len_result/", response_class=HTMLResponse, name='rectangle_len_result')
async def len_result(request: Request, a: str, b: str):
    new_rec = Rectangle(a=a, b=b)
    result = new_rec.get_perimeter()
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/rectangle_len.html", context={"result": result}
    )