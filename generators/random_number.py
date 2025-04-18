from starlette.responses import HTMLResponse
from generators.models import RandomNumber
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates


class RandomNumberApi:

    def __init__(self):
        self.router = APIRouter(prefix='/random_number', tags=['RandomNumber'])
        self.templates = Jinja2Templates(directory="templates")
        self.context: dict = {}

        @self.router.get("", response_class=HTMLResponse, name='random_number')
        async def random_number(request: Request):
            self.context.pop('result', None)
            self.context.update(
                {'title': 'Генератор случайных чисел | ',
                 'h1': 'Генератор случайных чисел',
                 'h2': 'подобрать случайные числа легко',
                 'action': 'random_number_result'},
                )
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="generators/random_number.html", context=self.context)

        @self.router.get("/result/", response_class=HTMLResponse, name='random_number_result')
        async def result(request: Request):

            count = int(request.query_params.get('count'))
            start = int(request.query_params.get('start'))
            stop = int(request.query_params.get('stop'))
            sorting = bool(request.query_params.get('sorting'))

            new_numbers = RandomNumber(count=count,
                                         start=start,
                                         stop=stop,
                                         sorting=sorting)

            result = new_numbers.create_numbers()
            self.context["result"] = result
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="generators/random_number.html", context=self.context)
