from starlette.responses import HTMLResponse
from generators.models import Password
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates


class PasswordApi:

    def __init__(self):
        self.router = APIRouter(prefix='/password', tags=['Password'])
        self.templates = Jinja2Templates(directory="templates")
        self.context: dict = {}

        @self.router.get("", response_class=HTMLResponse, name='password')
        async def password(request: Request):
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Генератор паролей ',
                 'h1': 'Генератор паролей онлайн',
                 'h2': 'подобрать пароль легко',
                 'h3': 'Сгенерированные пароли',
                 'action': 'password_result'},
                )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="generators/password.html", context=self.context)

        @self.router.get("/result/", response_class=HTMLResponse, name='password_result')
        async def result(request: Request):

            ascii_low = bool(request.query_params.get('ascii_low'))
            ascii_upp = bool(request.query_params.get('ascii_upp'))
            symbols = bool(request.query_params.get('symbols'))
            count = int(request.query_params.get('count'))
            length = int(request.query_params.get('length'))

            new_passwords = Password(count=count,
                                     length=length,
                                     ascii_low=ascii_low,
                                     ascii_upp=ascii_upp,
                                     symbols=symbols)

            result = new_passwords.create_pass()
            self.context["result"] = result
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="generators/password.html", context=self.context)
