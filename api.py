import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from api_geometry import router as math_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(math_router)


@app.get("/", response_class=HTMLResponse, name='home_page')
def home_page(request: Request, category: int = 1, limit: int = 6):
    headers = {1: 'Геометрические калькуляторы',
               2: 'Финансовые калькуляторы',
               3: 'Строительные калькуляторы',
               4: 'Конвертеры величин',
               5: 'Генераторы', }

    header_h1 = headers.get(category, 'Заголовок H1')

    # ToDo Подключить БД
    fake_db = [{'category': 1, 'name': 'Площадь круга', 'slug': 'circle_area', 'image': 'images/circle_s.png'},
               {'category': 1, 'name': 'Длина круга', 'slug': 'circle_len', 'image': 'images/circle_l.png'},
               {'category': 1, 'name': 'Площадь прямоугольника', 'slug': 'circle_area', 'image': 'images/pr_s.png'},
               {'category': 1, 'name': 'Периметр прямоугольника', 'slug': 'circle_len', 'image': 'images/pr_l.png'},
               {'category': 1, 'name': 'Площадь прямоугольного треугольника', 'slug': 'circle_area',
                'image': 'images/tr1_s.png'},
               {'category': 1, 'name': 'Гипотенуза прямоугольного треугольника', 'slug': 'circle_area',
                'image': 'images/tr1_g.png'},
               {'category': 1, 'name': 'Площадь равнобедренного треугольника', 'slug': 'circle_len',
                'image': 'images/tr3_s.png'},
               {'category': 1, 'name': 'Площадь равностороннего треугольника', 'slug': 'circle_len',
                'image': 'images/tr2_s.png'},
               {'category': 1, 'name': 'Высота равностороннего треугольника', 'slug': 'circle_area',
                'image': 'images/tr2_h.png'},
               {'category': 1, 'name': 'Площадь квадрата', 'slug': 'circle_area', 'image': 'images/kv_s.png'},
               {'category': 1, 'name': 'Периметр квадрата', 'slug': 'circle_area', 'image': 'images/kv_p.png'},
               {'category': 1, 'name': 'Площадь ромба', 'slug': 'circle_area', 'image': 'images/kv_s.png'},
               {'category': 1, 'name': 'Периметр ромба', 'slug': 'circle_area', 'image': 'images/kv_p.png'},
               {'category': 1, 'name': 'Площадь трапеции', 'slug': 'circle_area', 'image': 'images/kv_s.png'},
               {'category': 1, 'name': 'Периметр трапеции', 'slug': 'circle_area', 'image': 'images/kv_p.png'},

               ]

    filter_data = [i for i in fake_db if i['category'] == category][:limit]
    # Получить данные
    return templates.TemplateResponse(
        request=request, name="home.html", context={"h1": header_h1, "links": filter_data, 'category': category}
    )


if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
