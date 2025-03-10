from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

from geometry.models import Rhombus

router = APIRouter(prefix='/rhombus', tags=['Rhombus'])
templates = Jinja2Templates(directory="templates")


@router.get("/rhombus_area/", response_class=HTMLResponse, name='romb_area')
def rhombus_area(request: Request):

    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/rhombus_area.html", context={"similar_pages": []}
    )


@router.get("/romb_area_result/", response_class=HTMLResponse, name='romb_area_result')
async def rhombus_area_result(request: Request, a: str, h: str):
    new_rec = Rhombus(a=a, h=h)
    result = await new_rec.get_area()
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="geometry/rhombus_area.html", context={"result": result}
    )

