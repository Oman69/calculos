from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates


class CurrencyApi:

    def __init__(self):
        self.router = APIRouter(prefix='/currency', tags=['Currency'])
        self.templates = Jinja2Templates(directory="templates")
        self.context: dict = {}

        @self.router.get("", response_class=HTMLResponse, name='currency')
        async def currency(request: Request):

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/base.html", context=self.context)