from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from geometry.models import Trap

router = APIRouter(prefix='/trap', tags=['Trap'])
templates = Jinja2Templates(directory="templates")


@router.get("/area/", response_class=HTMLResponse, name='trap_area')
def area(request: Request):

    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/trap_area.html", context={"similar_pages": []}
    )


@router.get("/area_result/", response_class=HTMLResponse, name='trap_area_result')
async def area_result(request: Request, a: float, b: float, h: float):
    new_trap = Trap(a=a, b=b, h=h)
    result = new_trap.get_area()
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/trap_area.html", context={"result": result}
    )


@router.get("/perimeter/", response_class=HTMLResponse, name='trap_perimeter')
def perimeter(request: Request):

    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/trap_perimeter.html", context={"similar_pages": []}
    )


@router.get("/perimeter_result/", response_class=HTMLResponse, name='trap_perimeter_result')
async def perimeter_result(request: Request, a: float, b: float, c: float, d: float):
    new_trap = Trap(a=a, b=b, c=c, d=d)
    result = new_trap.get_perimeter()
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/trap_perimeter.html", context={"result": result}
    )
