from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

from geometry.models import Rhombus

router = APIRouter(prefix='/rhombus', tags=['Rhombus'])
templates = Jinja2Templates(directory="templates")


@router.get("/area/", response_class=HTMLResponse, name='rhombus_area')
def area(request: Request):

    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/rhombus_area.html", context={"similar_pages": []}
    )


@router.get("/area_result/", response_class=HTMLResponse, name='rhombus_area_result')
async def area_result(request: Request, a: str, h: str):
    new_rec = Rhombus(a=a, h=h)
    result = new_rec.get_area()
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/rhombus_area.html", context={"result": result}
    )


@router.get("/perimeter/", response_class=HTMLResponse, name='rhombus_perimeter')
def perimeter(request: Request):

    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/rhombus_perimeter.html", context={"similar_pages": []}
    )


@router.get("/perimeter_result/", response_class=HTMLResponse, name='rhombus_perimeter_result')
async def perimeter_result(request: Request, a: str):
    new_rec = Rhombus(a=a)
    result = new_rec.get_perimeter()
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/rhombus_perimeter.html", context={"result": result}
    )
