from db_structure import pages, engine
from sqlalchemy import select


async def get_similar_page(search_str: str):
    query = select(pages).where(pages.c.name.like(search_str + "%"))
    with engine.connect() as conn:
        data = [row for row in conn.execute(query)]
        return data