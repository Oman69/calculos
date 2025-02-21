from geometry.models import Circle
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from .circle import router as circle_router
from .rectangle import router as rec_router

router = APIRouter(prefix='/geometry', tags=['Geometry'])
templates = Jinja2Templates(directory="templates")

router.include_router(circle_router)
router.include_router(rec_router)



# @router.get("/rectangle_area/", response_class=HTMLResponse, name='rectangle_area')
# def rectangle_area(request: Request):
#
#     # Получить данные
#     return templates.TemplateResponse(
#         request=request, name="geometry/circle_area.html", context={"similar_pages": 1}
#     )
#
#
# @router.get("/rectangle_area_result/", response_class=HTMLResponse, name='rectangle_area_result')
# async def rectangle_area_result(request: Request, radius: str):
#     circle = Circle(radius=radius)
#     result = circle.get_area()
#     # Получить данные
#     return templates.TemplateResponse(
#         request=request, name="geometry/circle_area.html", context={"result": result}
#     )
#
#
# @router.get("/rectangle_len/", response_class=HTMLResponse, name='rectangle_len')
# def rectangle_len(request: Request):
#     # Получить данные
#     return templates.TemplateResponse(
#         request=request, name="geometry/circle_len.html", context={"id": 12}
#     )
#
#
# @router.get("/rectangle_len_result/", response_class=HTMLResponse, name='rectangle_len_result')
# async def rectangle_len_result(request: Request, radius: str):
#     circle = Circle(radius=radius)
#     result = circle.get_length()
#     # Получить данные
#     return templates.TemplateResponse(
#         request=request, name="geometry/circle_len.html", context={"result": result}
#     )