from starlette.responses import HTMLResponse
from geometry.models import Square
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

router = APIRouter(prefix='/square', tags=['Square'])
templates = Jinja2Templates(directory="templates")


@router.get("/area/", response_class=HTMLResponse, name='square_area')
def area(request: Request):

    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/square_area.html", context={"similar_pages": []}
    )


@router.get("/area_result/", response_class=HTMLResponse, name='square_area_result')
async def area_result(request: Request, a: float):
    new_square = Square(a=a)
    result = new_square.get_area()
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/square_area.html", context={"result": result}
    )


@router.get("/len/", response_class=HTMLResponse, name='square_len')
def len(request: Request):
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/square_len.html", context={"id": 12}
    )


@router.get("/len_result/", response_class=HTMLResponse, name='square_len_result')
async def len_result(request: Request, a: float):
    new_square = Square(a=a)
    result = new_square.get_perimeter()
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/square_len.html", context={"result": result}
    )