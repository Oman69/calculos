from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates


class DistanceApi:

    def __init__(self):
        self.router = APIRouter(prefix='/distance', tags=['Distance'])
        self.templates = Jinja2Templates(directory="templates")
        self.context: dict = {}

        @self.router.get("", response_class=HTMLResponse, name='distance')
        async def distance(request: Request):

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/base.html", context=self.context)