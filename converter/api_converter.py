from fastapi import APIRouter

from converter.currency import CurrencyApi
from converter.distance.distance import distance_api
from converter.area import AreaApi
from converter.weight.weight import weight_api

router = APIRouter(prefix='/converter', tags=['Converter'])

router.include_router(weight_api.router)
router.include_router(distance_api.router)
router.include_router(CurrencyApi().router)
router.include_router(AreaApi().router)

