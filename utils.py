from db_structure import pages, engine, converter_pages
from sqlalchemy import select

def select_main_pages_by_category(category: int, limit: int = None):
    query = select(pages).where(pages.c.category == category)
    filter_pages = []
    with engine.connect() as conn:
        for row in conn.execute(query):
            filter_pages.append(row.t)

    if limit:
        return filter_pages[:limit]
    return filter_pages


def select_converter_pages_by_category(category: int, limit: int = None):

    query = select(converter_pages).where(converter_pages.c.category == category)
    filter_pages = []
    with engine.connect() as conn:
        for row in conn.execute(query):
            filter_pages.append(row.t)

    if limit:
        return filter_pages[:limit]
    return filter_pages


def search_by_query(query: str):
    query = select(pages).where(pages.c.name.icontains(query))
    filter_pages = []
    with engine.connect() as conn:
        for row in conn.execute(query):
            filter_pages.append(row.t)
    return filter_pages


def search_by_tag(tag: str, cat_num: int):
    query = select(converter_pages).where(converter_pages.c.name.icontains(tag), converter_pages.c.category == cat_num)
    filter_pages = []
    with engine.connect() as conn:
        for row in conn.execute(query):
            filter_pages.append(row.t)
    return filter_pages


async def get_similar_page(search_str: str):
    query = select(pages).where(pages.c.name.like(search_str + "%"))
    with engine.connect() as conn:
        data = [row for row in conn.execute(query)]
        return data