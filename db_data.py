from sqlalchemy import insert
from db_structure import pages, engine

IMAGE_FOLDER = '/images/'


def insert_to_db(table, params):
    """

    :param table:
    :param params:
    :return:
    """
    query = insert(table).values(**params)
    with engine.connect() as conn:
        result = conn.execute(query)
        conn.commit()



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
           {'category': 1, 'name': 'Площадь куба', 'slug': 'circle_area', 'image': 'images/kb_s.png'},

           ]

# insert_to_db(pages, {'name': "Площадь круга", 'slug': "circle_area", 'category': 1, 'image':IMAGE_FOLDER + 'circle_s.png'})
# insert_to_db(pages, {'name': "Длина круга", 'slug': "circle_len", 'category': 1, 'image': IMAGE_FOLDER + 'circle_l.png'})
# insert_to_db(pages, {'name': "Площадь прямоугольника", 'slug': "rectangle_area", 'category': 1, 'image': IMAGE_FOLDER + 'pr_s.png'})
# insert_to_db(pages, {'name': "Площадь прямоугольника", 'slug': "rectangle_area", 'category': 1, 'image': IMAGE_FOLDER + 'pr_s.png'})
insert_to_db(pages, {'name': "Площадь прямоугольного треугольника", 'slug': "right_triangle_area", 'category': 1, 'image': IMAGE_FOLDER + 'tr1_s.png'})
insert_to_db(pages, {'name': "Гипотенуза прямоугольного треугольника", 'slug': "right_triangle_hypotenuse", 'category': 1, 'image': IMAGE_FOLDER + 'tr1_g.png'})
