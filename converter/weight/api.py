from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request, Body
from starlette.templating import Jinja2Templates
import utils
from converter.weight.models import Microgram, Milligram, Gram, Kilogram, Centner, Ton


class WeightApi:

    def __init__(self):
        self.router = APIRouter(prefix='/weight', tags=['Weight'])
        self.templates = Jinja2Templates(directory="templates")
        self.context = {}

        @self.router.get("", response_class=HTMLResponse, name='weight')
        async def view_weight_pages(request: Request, limit: int = 6):

            cat_num = 31
            filter_pages = utils.select_converter_pages_by_category(cat_num, limit)

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="files.html", context={'links': filter_pages,
                                                            'title': 'Вес и масса ',
                                                            'h1': 'Вес и масса',
                                                            'tags': ('G', 'MG', 'MKG', 'KG', 'T', 'C',),
                                                            'page': 'weight-input',
                                                            'category': cat_num})

        @self.router.get("/", response_class=HTMLResponse, name='weight-input')
        async def weight(request: Request, ff: str, tf: str):

            main_texts = {
                'pdf-jpeg': 1,
            }

            formats_str = {
                'g': 'Грамм',
                'mg': 'Милиграмм',
                'mkg': 'Микрограмм',
                'kg': 'Килогамм',
                'c': 'Центнер',
                't': 'Тонн',
            }

            from_str = formats_str[ff]
            to_str = formats_str[tf]

            self.context = {'title': f'Сколько {to_str.lower()} в {from_str.lower()}е',
                         'h1': f'{from_str}ы в {to_str.lower()}ы',
                         'h3': f'Итого {to_str.lower()}',
                         'action': 'weight-result',
                         'page': 'weight-input',
                         'item_name': f'{from_str}ы',
                         "main_text": '',
                         'formats': formats_str,
                         'ff': ff,
                         'tf': tf}

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/result/", response_class=HTMLResponse, name='weight-result')
        async def convert(request: Request, ff: str, tf: str, value: float):

            formats_models = {
                'mkg': Microgram,
                'mg': Milligram,
                'g': Gram,
                'kg': Kilogram,
                'c': Centner,
                't': Ton,
            }

            model = formats_models.get(ff, Gram)

            item = model(value=value, item_change=tf)
            result = item.convert()
            self.context.update({'result': result, 'value': value})
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)


weight_api = WeightApi()
