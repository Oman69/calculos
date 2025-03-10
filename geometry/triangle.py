from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

from geometry.models import RightTriangle, IsoscelesTriangle

router = APIRouter(prefix='/triangle', tags=['Triangle'])
templates = Jinja2Templates(directory="templates")


@router.get("/right_triangle_area/", response_class=HTMLResponse, name='right_triangle_area')
def right_triangle_area(request: Request):

    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/right_triangle_area.html", context={"similar_pages": []}
    )


@router.get("/right_triangle_area_result/", response_class=HTMLResponse, name='right_triangle_area_result')
async def right_triangle_area_result(request: Request, a: str, b: str):
    new_rec = RightTriangle(a=a, b=b)
    result = new_rec.get_area()
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/right_triangle_area.html", context={"result": result}
    )


@router.get("/right_triangle_hypotenuse/", response_class=HTMLResponse, name='right_triangle_hypotenuse')
def right_triangle_hypotenuse(request: Request):
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/right_triangle_hypotenuse.html", context={"id": 12}
    )


@router.get("/right_triangle_hypotenuse_result/", response_class=HTMLResponse, name='right_triangle_hypotenuse_result')
async def right_triangle_hypotenuse_result(request: Request, a: str, b: str):
    new_rec = RightTriangle(a=a, b=b)
    result = new_rec.get_hypotenuse()
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/right_triangle_hypotenuse.html", context={"result": result}
    )


@router.get("/isosceles_triangle_area/", response_class=HTMLResponse, name='isosceles_triangle_area')
def isosceles_triangle_area(request: Request):

    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/isosceles_triangle_area.html", context={"similar_pages": []}
    )


@router.get("/isosceles_triangle_area_result/", response_class=HTMLResponse, name='isosceles_triangle_area_result')
async def isosceles_triangle_area_result(request: Request, h: str, c: str):
    new_tr = IsoscelesTriangle(h=h, c=c)
    result = new_tr.get_area()
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/isosceles_triangle_area.html", context={"result": result}
    )

