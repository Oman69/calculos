from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request, Body
from starlette.templating import Jinja2Templates
import utils
from converter.area.models import *


class AreaApi:
    """
    Класс конвертера "Площадь"
    """

    def __init__(self):
        self.router = APIRouter(prefix='/area', tags=['Area'])
        self.templates = Jinja2Templates(directory="templates")
        self.context = {}
        self.formats_models = {
                'cm': Centimeter,
                'dm': Decimeter,
                'm': Meter,
                'km': Kilometer,
                'in': Inch,
                'ft': Foot,
                'akr': Akr,
                'ga': Hectare

            }

        @self.router.get("", response_class=HTMLResponse, name='area')
        async def view_pages(request: Request, limit: int = 6):

            cat_num = 33
            filter_pages = utils.select_converter_pages_by_category(cat_num, limit)

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="files.html", context={'links': filter_pages,
                                                            'title': 'Площадь ',
                                                            'h1': 'Площадь',
                                                            'tags': ('MM', 'CM', 'DM', 'M', 'KM', 'FT'),
                                                            'page': 'area-input',
                                                            'category': cat_num})

        @self.router.get("/", response_class=HTMLResponse, name='area-input')
        async def data_input(request: Request, ff: str, tf: str):

            main_texts = {
                'pdf-jpeg': 1,
            }

            from_str = self.formats_models[ff]().view_str()
            to_str = self.formats_models[tf]().view_str()

            self.context = {'title': f'Сколько {to_str.lower()}ов в {from_str.lower()}е',
                         'h1': f'{from_str}ы в {to_str.lower()}ы',
                         'h3': f'Итого {to_str.lower()}ов',
                         'action': 'area-result',
                         'page': 'area-input',
                         'item_name': f'{from_str}ы',
                         "main_text": main_texts.get(ff + '-' + tf, 'Описание'),
                         'formats': [(key, value().view_str()) for key, value in self.formats_models.items()],
                         'ff': ff,
                         'tf': tf}

            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)

        @self.router.get("/result/", response_class=HTMLResponse, name='area-result')
        async def convert(request: Request, ff: str, tf: str, value: float):

            model = self.formats_models.get(ff, Centimeter)

            item = model(value=value, item_change=tf)
            result = item.convert()
            self.context.update({'result': result, 'value': value})
            # Получить данные
            return self.templates.TemplateResponse(
                request=request, name="converter/converter.html", context=self.context)


area_api = AreaApi()
