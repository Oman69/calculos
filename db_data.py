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


# insert_to_db(pages, {'name': "Площадь круга", 'slug': "circle_area", 'category': 1, 'image':IMAGE_FOLDER + 'circle_s.png'})
# insert_to_db(pages, {'name': "Длина круга", 'slug': "circle_len", 'category': 1, 'image': IMAGE_FOLDER + 'circle_l.png'})
# insert_to_db(pages, {'name': "Площадь прямоугольника", 'slug': "rectangle_area", 'category': 1, 'image': IMAGE_FOLDER + 'pr_s.png'})
# insert_to_db(pages, {'name': "Периметр прямоугольника", 'slug': "rectangle_len", 'category': 1, 'image': IMAGE_FOLDER + 'pr_l.png'})
# insert_to_db(pages, {'name': "Диагональ прямоугольника", 'slug': "rectangle_diag", 'category': 1, 'image': IMAGE_FOLDER + 'pr_d.png'})
# insert_to_db(pages, {'name': "Площадь квадрата", 'slug': "square_area", 'category': 1, 'image': IMAGE_FOLDER + 'kv_s.png'})
# insert_to_db(pages, {'name': "Периметр квадрата", 'slug': "square_len", 'category': 1, 'image': IMAGE_FOLDER + 'kv_p.png'})
# insert_to_db(pages, {'name': "Диагональ квадрата", 'slug': "square_diag", 'category': 1, 'image': IMAGE_FOLDER + 'kv_d.png'})
# insert_to_db(pages, {'name': "Площадь прямоугольного треугольника", 'slug': "right_triangle_area", 'category': 1, 'image': IMAGE_FOLDER + 'tr1_s.png'})
# insert_to_db(pages, {'name': "Гипотенуза прямоугольного треугольника", 'slug': "right_triangle_hypotenuse", 'category': 1, 'image': IMAGE_FOLDER + 'tr1_g.png'})
# insert_to_db(pages, {'name': "Площадь равнобедренного треугольника", 'slug': "isosceles_triangle_area", 'category': 1, 'image': IMAGE_FOLDER + 'tr3_s.png'})
# insert_to_db(pages, {'name': "Площадь ромба", 'slug': "rhombus_area", 'category': 1, 'image': IMAGE_FOLDER + 'rhombus_s.png'})
# insert_to_db(pages, {'name': "Периметр ромба", 'slug': "rhombus_perimeter", 'category': 1, 'image': IMAGE_FOLDER + 'rhombus_h.png'})
# insert_to_db(pages, {'name': "Площадь равностороннего треугольника", 'slug': "equ_triangle_area", 'category': 1, 'image': IMAGE_FOLDER + 'tr2_s.png'})
# insert_to_db(pages, {'name': "Высота равностороннего треугольника", 'slug': "equ_triangle_height", 'category': 1, 'image': IMAGE_FOLDER + 'tr2_h.png'})
# insert_to_db(pages, {'name': "Площадь трапеции", 'slug': "trap_area", 'category': 1, 'image': IMAGE_FOLDER + 'trap_s.png'})
# insert_to_db(pages, {'name': "Периметр трапеции", 'slug': "trap_perimeter", 'category': 1, 'image': IMAGE_FOLDER + 'trap_p.png'})
# insert_to_db(pages, {'name': "Площадь куба", 'slug': "cube_area", 'category': 1, 'image': IMAGE_FOLDER + 'cube_s.png'})
# insert_to_db(pages, {'name': "Высота равнобедренного треугольника", 'slug': "isosceles_triangle_height", 'category': 1, 'image': IMAGE_FOLDER + 'tr3_h.png'})
# insert_to_db(pages, {'name': "Объем куба", 'slug': "cube_volume", 'category': 1, 'image': IMAGE_FOLDER + 'cube_v.png'})
# insert_to_db(pages, {'name': "Периметр трапеции", 'slug': "trap_perimeter", 'category': 1, 'image': IMAGE_FOLDER + 'trap_p.png'})

# insert_to_db(pages, {'name': "Вес и масса", 'slug': "weight", 'category': 3, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Расстояние и длина", 'slug': "distance", 'category': 3, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Валюты", 'slug': "currency", 'category': 3, 'image': IMAGE_FOLDER + 'currency_i.png'})
# insert_to_db(pages, {'name': "Площадь", 'slug': "square", 'category': 3, 'image': IMAGE_FOLDER + 'square_i.png'})
# insert_to_db(pages, {'name': "Граммы в Килограммы", 'slug': "gram_kilogram", 'category': 31, 'image': IMAGE_FOLDER + 'square_i.png'})
insert_to_db(pages, {'name': "Килограммы в Граммы", 'slug': "kilogram_gram", 'category': 31, 'image': IMAGE_FOLDER + 'square_i.png'})