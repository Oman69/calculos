from fastapi import APIRouter

from converter.distance.api import distance_api
from converter.area.api import area_api
from converter.files.files import files_converter_api
from converter.weight.api import weight_api

router = APIRouter(prefix='/converter', tags=['Converter'])

router.include_router(weight_api.router)
router.include_router(distance_api.router)
router.include_router(area_api.router)
router.include_router(files_converter_api.router)

