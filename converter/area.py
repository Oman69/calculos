from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates


class AreaApi:

    def __init__(self):
        self.router = APIRouter(prefix='/area', tags=['Area'])
        self.templates = Jinja2Templates(directory="templates")

        @self.router.get("", response_class=HTMLResponse, name='area')
        async def area(request: Request):

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/base.html", context={})
