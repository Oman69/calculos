import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from geometry.api_geometry import router as math_router
from converter.api_converter import router as converter_router
import utils

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(math_router)
app.include_router(converter_router)


@app.get("/", response_class=HTMLResponse, name='home_page')
def home_page(request: Request, category: int = 1, limit: int = 6):
    headers = {1: 'Геометрические калькуляторы',
               2: 'Финансовые калькуляторы',
               3: 'Конвертеры величин',
               4: 'Генераторы', }

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


@app.get("/search/", response_class=HTMLResponse, name='search_page')
def search_page(request: Request, query: str):

    filter_pages = utils.search_by_query(query)

    # Получить данные
    return templates.TemplateResponse(
        request=request, name="search.html",
        context={"links": filter_pages}
    )


if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
