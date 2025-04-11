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
                {'title': 'Генератор паролей | ',
                 'h1': 'Генератор паролей онлайн',
                 'h2': 'подобрать пароль легко',
                 'h3': 'Сгенерированные пароли',
                 'action': 'password_result'},
                )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="generators/password.html", context=self.context)

        @self.router.get("/result/", response_class=HTMLResponse, name='password_result')
        async def result(request: Request,
                              count: int = 3,
                              length: int = 6,
                              ascii_low: bool = True,
                              ascii_upp: bool = True,
                              symbols: bool = True):

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
