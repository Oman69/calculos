from fastapi import APIRouter
from generators.passwords import PasswordApi
from generators.random_number import RandomNumberApi

router = APIRouter(prefix='/generators', tags=['Generators'])


router.include_router(PasswordApi().router)
router.include_router(RandomNumberApi().router)
