from fastapi import APIRouter
from .circle import CircleApi
from .equ_triangle import EquTriangleApi
from .iso_triangle import IsoTriangleApi
from .rhombus import RhombusApi
from .cube import CubeApi
from .right_triangle import RightTriangleApi
from .square import SquareApi
from .rectangle import RectangleApi
from .trap import TrapApi

router = APIRouter(prefix='/geometry', tags=['Geometry'])

router.include_router(CircleApi().router)
router.include_router(RhombusApi().router)
router.include_router(CubeApi().router)
router.include_router(TrapApi().router)
router.include_router(SquareApi().router)
router.include_router(RectangleApi().router)
router.include_router(RightTriangleApi().router)
router.include_router(EquTriangleApi().router)
router.include_router(IsoTriangleApi().router)
