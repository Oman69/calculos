from fastapi import APIRouter
from starlette.templating import Jinja2Templates
from .circle import router as circle_router
from .rectangle import router as rec_router
from .square import router as square_router
from .triangle import router as triangle_router
from .rhombus import router as rhombus_router
from .trap import router as trap_router

router = APIRouter(prefix='/geometry', tags=['Geometry'])
templates = Jinja2Templates(directory="templates")

router.include_router(circle_router)
router.include_router(rec_router)
router.include_router(square_router)
router.include_router(triangle_router)
router.include_router(rhombus_router)
router.include_router(trap_router)