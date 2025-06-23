from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request, Body
from starlette.templating import Jinja2Templates
import utils
from converter.distance.models import *


class DistanceApi:

    def __init__(self):
        self.router = APIRouter(prefix='/distance', tags=['Distance'])
        self.templates = Jinja2Templates(directory="templates")
        self.context = {}
        self.formats_models = {
                'mm': Millimeter,
                'cm': Centimeter,
                'dm': Decimeter,
                'm': Meter,
                'km': Kilometer,
                'in': Inch,
                'ft': Foot,
                'ya': Yard,
            }

        @self.router.get("", response_class=HTMLResponse, name='distance')
        async def view_pages(request: Request, limit: int = 6):

            cat_num = 32
            filter_pages = utils.select_converter_pages_by_category(cat_num, limit)

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="files.html", context={'links': filter_pages,
                                                            'title': 'Расстояние и длина ',
                                                            'h1': 'Расстояние и длина',
                                                            'tags': ('MM', 'CM', 'DM', 'M', 'KM', 'ML', 'FT'),
                                                            'page': 'distance-input',
                                                            'category': cat_num})

        @self.router.get("/", response_class=HTMLResponse, name='distance-input')
        async def data_input(request: Request, ff: str, tf: str):

            main_texts = {
                'pdf-jpeg': 1,
            }

            from_str = self.formats_models[ff]().view_str()
            to_str = self.formats_models[tf]().view_str()

            self.context = {'title': f'Сколько {to_str.lower()}ов в {from_str.lower()}е',
                         'h1': f'{from_str}ы в {to_str.lower()}ы',
                         'h3': f'Итого {to_str.lower()}ов',
                         'action': 'distance-result',
                         'page': 'distance-input',
                         'item_name': f'{from_str}ы',
                         "main_text": '',
                         'formats': [(key, value().view_str()) for key, value in self.formats_models.items()],
                         'ff': ff,
                         'tf': tf}

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/result/", response_class=HTMLResponse, name='distance-result')
        async def convert(request: Request, ff: str, tf: str, value: float):

            model = self.formats_models.get(ff, Millimeter)

            item = model(value=value, item_change=tf)
            result = item.convert()
            self.context.update({'result': result, 'value': value})
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)


distance_api = DistanceApi()
