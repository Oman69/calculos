from fastapi import APIRouter

from converter.currency import CurrencyApi
from converter.distance import DistanceApi
from converter.area import AreaApi
from converter.weight import WeightApi

router = APIRouter(prefix='/converter', tags=['Converter'])

router.include_router(WeightApi().router)
router.include_router(DistanceApi().router)
router.include_router(CurrencyApi().router)
router.include_router(AreaApi().router)

