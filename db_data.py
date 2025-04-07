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
# insert_to_db(pages, {'name': "Граммы в Килограммы", 'slug': "gram_kilogram", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Граммы в Милиграммы", 'slug': "g_mg", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Граммы в Микрограммы", 'slug': "g_mkg", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Граммы в Центнеры", 'slug': "g_c", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Граммы в Тонны", 'slug': "g_t", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Граммы в Караты", 'slug': "g_k", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})

# insert_to_db(pages, {'name': "Килограммы в Граммы", 'slug': "kg_g", 'category': 31, 'image': IMAGE_FOLDER + 'kg_i.png'})
# insert_to_db(pages, {'name': "Килограммы в Милиграммы", 'slug': "kg_mg", 'category': 31, 'image': IMAGE_FOLDER + 'kg_i.png'})
# insert_to_db(pages, {'name': "Килограммы в Микрограммы", 'slug': "kg_mkg", 'category': 31, 'image': IMAGE_FOLDER + 'kg_i.png'})
# insert_to_db(pages, {'name': "Килограммы в Центнеры", 'slug': "kg_c", 'category': 31, 'image': IMAGE_FOLDER + 'kg_i.png'})
# insert_to_db(pages, {'name': "Килограммы в Тонны", 'slug': "kg_t", 'category': 31, 'image': IMAGE_FOLDER + 'kg_i.png'})
# insert_to_db(pages, {'name': "Килограммы в Караты", 'slug': "kg_k", 'category': 31, 'image': IMAGE_FOLDER + 'kg_i.png'})

# insert_to_db(pages, {'name': "Милиграммы в Граммы", 'slug': "mg_g", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Милиграммы в Килограммы", 'slug': "mg_kg", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Милиграммы в Микрограммы", 'slug': "mg_mkg", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Милиграммы в Центнеры", 'slug': "mg_c", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Милиграммы в Тонны", 'slug': "mg_t", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Милиграммы в Караты", 'slug': "mg_k", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})

# insert_to_db(pages, {'name': "Микрограммы в Граммы", 'slug': "mkg_g", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Микрограммы в Килограммы", 'slug': "mkg_kg", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Микрограммы в Милиграммы", 'slug': "mkg_mg", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Микрограммы в Центнеры", 'slug': "mkg_c", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Микрограммы в Тонны", 'slug': "mkg_t", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Микрограммы в Караты", 'slug': "mkg_k", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})


# insert_to_db(pages, {'name': "Центнеры в Граммы", 'slug': "c_g", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Центнеры в Килограммы", 'slug': "c_kg", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Центнеры в Милиграммы", 'slug': "c_mg", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Центнеры в Микрограммы", 'slug': "c_mkg", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Центнеры в Тонны", 'slug': "c_t", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Центнеры в Караты", 'slug': "c_k", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})


# insert_to_db(pages, {'name': "Тонны в Граммы", 'slug': "t_g", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Тонны в Килограммы", 'slug': "t_kg", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Тонны в Милиграммы", 'slug': "t_mg", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Тонны в Микрограммы", 'slug': "t_mkg", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Тонны в Центнеры", 'slug': "t_c", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Тонны в Караты", 'slug': "t_k", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})

# insert_to_db(pages, {'name': "Миллиметры в Сантиметры", 'slug': "mm_cm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Миллиметры в Дециметры", 'slug': "mm_dm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Миллиметры в Метры", 'slug': "mm_m", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Миллиметры в Килоиметры", 'slug': "mm_km", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Миллиметры в Дюймы", 'slug': "mm_inch", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Миллиметры в Футы", 'slug': "mm_ft", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})

# insert_to_db(pages, {'name': "Сантиметры в Миллиметры", 'slug': "cm_mm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Сантиметры в Дециметры", 'slug': "cm_dm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Сантиметры в Метры", 'slug': "cm_m", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Сантиметры в Килоиметры", 'slug': "cm_km", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Сантиметры в Дюймы", 'slug': "cm_inch", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Сантиметры в Футы", 'slug': "cm_ft", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})

insert_to_db(pages, {'name': "Дециметры в Миллиметры", 'slug': "dm_mm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
insert_to_db(pages, {'name': "Дециметры в Сантиметры", 'slug': "dm_cm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
insert_to_db(pages, {'name': "Дециметры в Метры", 'slug': "dm_m", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
insert_to_db(pages, {'name': "Дециметры в Килоиметры", 'slug': "dm_km", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
insert_to_db(pages, {'name': "Дециметры в Дюймы", 'slug': "dm_inch", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
insert_to_db(pages, {'name': "Дециметры в Футы", 'slug': "dm_ft", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
