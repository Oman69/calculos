import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from geometry.api_geometry import router as math_router
from db_structure import engine, pages

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(math_router)


def select_main_pages_by_category(category: int, limit: int):
    query = select(pages).where(pages.c.category == category)
    filter_pages = []
    with engine.connect() as conn:
        for row in conn.execute(query):
            filter_pages.append(row.t)

    return filter_pages[:limit]


@app.get("/", response_class=HTMLResponse, name='home_page')
def home_page(request: Request, category: int = 1, limit: int = 6):
    headers = {1: 'Геометрические калькуляторы',
               2: 'Финансовые калькуляторы',
               3: 'Строительные калькуляторы',
               4: 'Конвертеры величин',
               5: 'Генераторы', }

    header_h1 = headers.get(category, 'Заголовок H1')

    filter_pages = select_main_pages_by_category(category, limit)

    # Получить данные
    return templates.TemplateResponse(
        request=request, name="home.html",
        context={"h1": header_h1, "links": filter_pages, 'category': category}
    )


if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
