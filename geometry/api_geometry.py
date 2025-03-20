from fastapi import APIRouter
from .circle import CircleApi
from .rhombus import RhombusApi
from .cube import CubeApi
from .square import router as square_router
from .rectangle import router as rec_router
from .triangle import router as triangle_router
from .trap import TrapApi

router = APIRouter(prefix='/geometry', tags=['Geometry'])

router.include_router(CircleApi().router)
router.include_router(RhombusApi().router)
router.include_router(CubeApi().router)
router.include_router(TrapApi().router)
router.include_router(rec_router)
router.include_router(square_router)
router.include_router(triangle_router)
