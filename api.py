import os
import uuid

import uvicorn
from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from geometry.api_geometry import router as math_router
from converter.api_converter import router as converter_router
from generators.api_generators import router as generator_router
from fastapi.responses import PlainTextResponse
import utils

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.mount("/" + UPLOAD_DIR, StaticFiles(directory=UPLOAD_DIR), name=UPLOAD_DIR)
templates = Jinja2Templates(directory="templates")

app.include_router(math_router)
app.include_router(converter_router)
app.include_router(generator_router)


@app.get("/", response_class=HTMLResponse, name='home_page')
def home_page(request: Request, category: int = 1, limit: int = 6):
    headers = {1: 'Геометрические калькуляторы',
               3: 'Конвертеры величин',
               4: 'Генераторы'}

    header_h1 = headers.get(category, 'Заголовок H1')

    filter_pages = utils.select_main_pages_by_category(category, limit)

    context = {"h1": header_h1,
               "links": filter_pages,
               'category': category}

    # Получить данные
    return templates.TemplateResponse(
        request=request, name="home.html",
        context=context
    )


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    # Генерируем уникальное имя файла
    file_id = str(uuid.uuid4())
    # Получил разрешение
    file_ext = os.path.splitext(file.filename)[1]
    file_path = os.path.join(UPLOAD_DIR, f"{file_id}{file_ext}")

    # Сохраняем файл
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Возвращаем ссылку
    return {"file_url": f"/{UPLOAD_DIR}/{file_id}{file_ext}",
            "ext": file_ext}


@app.get("/search/", response_class=HTMLResponse, name='search_page')
def search_page(request: Request, query: str):

    filter_pages = utils.search_by_query(query)

    # Получить данные
    return templates.TemplateResponse(
        request=request, name="search.html",
        context={"links": filter_pages}
    )


@app.get("/sitemap/", response_class=HTMLResponse, name='sitemap')
def sitemap(request: Request):

    geometry_pages = utils.select_main_pages_by_category(category=1)
    generators_pages = utils.select_main_pages_by_category(category=4)
    weight_pages = utils.select_main_pages_by_category(category=31)
    distance_pages = utils.select_main_pages_by_category(category=32)
    area_pages = utils.select_main_pages_by_category(category=33)

    # Получить данные
    return templates.TemplateResponse(
        request=request, name="sitemap.html",
        context={"geometry_pages": geometry_pages,
                 'generators_pages': generators_pages,
                 'weight_pages': weight_pages,
                 'distance_pages': distance_pages,
                 'area_pages': area_pages}
    )


@app.get('/robots.txt', response_class=PlainTextResponse)
def robots():
    data = """User-agent: *\nClean-param: utm\nHost: https://calculos.ru\nSitemap: https://calculos.ru/sitemap.xml"""
    return data


if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
