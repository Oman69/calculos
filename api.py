import os
from typing import List

import uvicorn
from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse
from geometry.api_geometry import router as math_router
from converter.api_converter import router as converter_router
from generators.api_generators import router as generator_router
from fastapi.responses import PlainTextResponse
import utils

app = FastAPI()

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "output"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)


app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/" + UPLOAD_DIR, StaticFiles(directory=UPLOAD_DIR), name=UPLOAD_DIR)
app.mount("/" + OUTPUT_DIR, StaticFiles(directory=OUTPUT_DIR), name=OUTPUT_DIR)
templates = Jinja2Templates(directory="templates")

app.include_router(math_router)
app.include_router(converter_router)
app.include_router(generator_router)


@app.get("/", response_class=HTMLResponse, name='home_page')
def home_page(request: Request, category: int = 1, limit: int = 6):
    headers = {1: 'Геометрические калькуляторы',
               3: 'Конвертеры',
               4: 'Генераторы'}

    header_h1 = headers.get(category, 'Заголовок H1')

    filter_pages = utils.select_main_pages_by_category(category, limit)

    context = {"h1": header_h1,
               'title': header_h1,
               "links": filter_pages,
               'category': category}

    # Получить данные
    return templates.TemplateResponse(
        request=request, name="home.html",
        context=context
    )


@app.post("/upload/")
async def upload_file(files: List[UploadFile]):

    response_data = {}
    response_data.setdefault('file_urls', [])

    for file in files:
        # Получил путь к файлу
        file_path = os.path.join(UPLOAD_DIR, file.filename)

        # Сохраняем файл
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        response_data['file_urls'].append(f"/{UPLOAD_DIR}/{file.filename}")

    return response_data


@app.get("/download/{filename}", response_class=FileResponse)
async def download_file(filename: str):
    # Реализация кода для получения и возврата запрошенного файла
    file_path = os.path.join(OUTPUT_DIR, filename)
    return FileResponse(path=file_path)


@app.get("/search/", response_class=HTMLResponse, name='search_page')
def search_page(request: Request, query: str):

    filter_pages = utils.search_by_query(query)

    # Получить данные
    return templates.TemplateResponse(
        request=request, name="search.html",
        context={"links": filter_pages, 'h1': 'Результат поиска: ' + query}
    )


@app.get("/search_tag/", response_class=HTMLResponse, name='search_tag')
def search_tag(request: Request, tag: str, category_num: int):

    filter_pages = utils.search_by_tag(tag=tag, cat_num=category_num)

    # Получить данные
    return templates.TemplateResponse(
        request=request, name="search_tag.html",
        context={"links": filter_pages, 'h1': tag}
    )


@app.get("/sitemap/", response_class=HTMLResponse, name='sitemap')
def sitemap(request: Request):

    geometry_pages = utils.select_main_pages_by_category(category=1)
    generators_pages = utils.select_main_pages_by_category(category=4)
    weight_pages = utils.select_main_pages_by_category(category=31)
    distance_pages = utils.select_main_pages_by_category(category=32)
    area_pages = utils.select_main_pages_by_category(category=33)
    files_pages = utils.select_main_pages_by_category(category=5)

    # Получить данные
    return templates.TemplateResponse(
        request=request, name="sitemap.html",
        context={"geometry_pages": geometry_pages,
                 'generators_pages': generators_pages,
                 'weight_pages': weight_pages,
                 'distance_pages': distance_pages,
                 'area_pages': area_pages,
                 'files_pages': files_pages}
    )


@app.get('/robots.txt', response_class=PlainTextResponse)
def robots():
    data = """User-agent: *\nClean-param: utm\nHost: https://calculos.ru\nSitemap: https://calculos.ru/sitemap.xml"""
    return data


if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
