from fastapi import APIRouter
from generators.passwords import PasswordApi

router = APIRouter(prefix='/generators', tags=['Generators'])


router.include_router(PasswordApi().router)