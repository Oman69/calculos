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
# insert_to_db(pages, {'name': "Площадь равнобедренного треугольника", 'slug': "iso_triangle_area", 'category': 1, 'image': IMAGE_FOLDER + 'tr3_s.png'})
# insert_to_db(pages, {'name': "Площадь ромба", 'slug': "rhombus_area", 'category': 1, 'image': IMAGE_FOLDER + 'rhombus_s.png'})
# insert_to_db(pages, {'name': "Периметр ромба", 'slug': "rhombus_perimeter", 'category': 1, 'image': IMAGE_FOLDER + 'rhombus_p.png'})
# insert_to_db(pages, {'name': "Площадь равностороннего треугольника", 'slug': "equ_triangle_area", 'category': 1, 'image': IMAGE_FOLDER + 'tr2_s.png'})
# insert_to_db(pages, {'name': "Высота равностороннего треугольника", 'slug': "equ_triangle_height", 'category': 1, 'image': IMAGE_FOLDER + 'tr2_h.png'})
# insert_to_db(pages, {'name': "Площадь трапеции", 'slug': "trap_area", 'category': 1, 'image': IMAGE_FOLDER + 'trap_s.png'})
# insert_to_db(pages, {'name': "Периметр трапеции", 'slug': "trap_perimeter", 'category': 1, 'image': IMAGE_FOLDER + 'trap_p.png'})
# insert_to_db(pages, {'name': "Площадь куба", 'slug': "cube_area", 'category': 1, 'image': IMAGE_FOLDER + 'cube_s.png'})
# insert_to_db(pages, {'name': "Высота равнобедренного треугольника", 'slug': "iso_triangle_height", 'category': 1, 'image': IMAGE_FOLDER + 'tr3_h.png'})
# insert_to_db(pages, {'name': "Объем куба", 'slug': "cube_volume", 'category': 1, 'image': IMAGE_FOLDER + 'cube_v.png'})
#
# insert_to_db(pages, {'name': "Вес и масса", 'slug': "weight", 'category': 3, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Расстояние и длина", 'slug': "distance", 'category': 3, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Площадь", 'slug': "area", 'category': 3, 'image': IMAGE_FOLDER + 'square_i.png'})
#insert_to_db(pages, {'name': "Конвертеры файлов", 'slug': "files_converter", 'category': 3, 'image': IMAGE_FOLDER + 'square_i.png'})
#
# insert_to_db(pages, {'name': "Граммы в Килограммы", 'slug': "g_kg", 'category': 31, 'image': IMAGE_FOLDER + 'g_kg.png'})
# insert_to_db(pages, {'name': "Граммы в Милиграммы", 'slug': "g_mg", 'category': 31, 'image': IMAGE_FOLDER + 'g_mg.png'})
# insert_to_db(pages, {'name': "Граммы в Микрограммы", 'slug': "g_mkg", 'category': 31, 'image': IMAGE_FOLDER + 'g_mkg.png'})
# insert_to_db(pages, {'name': "Граммы в Центнеры", 'slug': "g_c", 'category': 31, 'image': IMAGE_FOLDER + 'g_c.png'})
# insert_to_db(pages, {'name': "Граммы в Тонны", 'slug': "g_t", 'category': 31, 'image': IMAGE_FOLDER + 'g_t.png'})
# insert_to_db(pages, {'name': "Граммы в Караты", 'slug': "g_k", 'category': 31, 'image': IMAGE_FOLDER + 'g_k.png'})
#
# insert_to_db(pages, {'name': "Килограммы в Граммы", 'slug': "kg_g", 'category': 31, 'image': IMAGE_FOLDER + 'kg_g.png'})
# insert_to_db(pages, {'name': "Килограммы в Милиграммы", 'slug': "kg_mg", 'category': 31, 'image': IMAGE_FOLDER + 'kg_mg.png'})
# insert_to_db(pages, {'name': "Килограммы в Микрограммы", 'slug': "kg_mkg", 'category': 31, 'image': IMAGE_FOLDER + 'kg_mkg.png'})
# insert_to_db(pages, {'name': "Килограммы в Центнеры", 'slug': "kg_c", 'category': 31, 'image': IMAGE_FOLDER + 'kg_c.png'})
# insert_to_db(pages, {'name': "Килограммы в Тонны", 'slug': "kg_t", 'category': 31, 'image': IMAGE_FOLDER + 'kg_t.png'})
# insert_to_db(pages, {'name': "Килограммы в Караты", 'slug': "kg_k", 'category': 31, 'image': IMAGE_FOLDER + 'kg_k.png'})
#
# insert_to_db(pages, {'name': "Милиграммы в Граммы", 'slug': "mg_g", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Милиграммы в Килограммы", 'slug': "mg_kg", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Милиграммы в Микрограммы", 'slug': "mg_mkg", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Милиграммы в Центнеры", 'slug': "mg_c", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Милиграммы в Тонны", 'slug': "mg_t", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Милиграммы в Караты", 'slug': "mg_k", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
#
# insert_to_db(pages, {'name': "Микрограммы в Граммы", 'slug': "mkg_g", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Микрограммы в Килограммы", 'slug': "mkg_kg", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Микрограммы в Милиграммы", 'slug': "mkg_mg", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Микрограммы в Центнеры", 'slug': "mkg_c", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Микрограммы в Тонны", 'slug': "mkg_t", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Микрограммы в Караты", 'slug': "mkg_k", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
#
#
# insert_to_db(pages, {'name': "Центнеры в Граммы", 'slug': "c_g", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Центнеры в Килограммы", 'slug': "c_kg", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Центнеры в Милиграммы", 'slug': "c_mg", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Центнеры в Микрограммы", 'slug': "c_mkg", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Центнеры в Тонны", 'slug': "c_t", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Центнеры в Караты", 'slug': "c_k", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
#
#
# insert_to_db(pages, {'name': "Тонны в Граммы", 'slug': "t_g", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Тонны в Килограммы", 'slug': "t_kg", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Тонны в Милиграммы", 'slug': "t_mg", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Тонны в Микрограммы", 'slug': "t_mkg", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Тонны в Центнеры", 'slug': "t_c", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Тонны в Караты", 'slug': "t_k", 'category': 31, 'image': IMAGE_FOLDER + 'weight_i.png'})
#
# insert_to_db(pages, {'name': "Миллиметры в Сантиметры", 'slug': "mm_cm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Миллиметры в Дециметры", 'slug': "mm_dm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Миллиметры в Метры", 'slug': "mm_m", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Миллиметры в Километры", 'slug': "mm_km", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Миллиметры в Дюймы", 'slug': "mm_inch", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Миллиметры в Футы", 'slug': "mm_ft", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Миллиметры в Ярды", 'slug': "mm_ya", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
#
# insert_to_db(pages, {'name': "Сантиметры в Миллиметры", 'slug': "cm_mm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Сантиметры в Дециметры", 'slug': "cm_dm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Сантиметры в Метры", 'slug': "cm_m", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Сантиметры в Километры", 'slug': "cm_km", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Сантиметры в Дюймы", 'slug': "cm_inch", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Сантиметры в Футы", 'slug': "cm_ft", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Сантиметры в Ярды", 'slug': "cm_ya", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
#
# insert_to_db(pages, {'name': "Дециметры в Миллиметры", 'slug': "dm_mm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Дециметры в Сантиметры", 'slug': "dm_cm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Дециметры в Метры", 'slug': "dm_m", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Дециметры в Километры", 'slug': "dm_km", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Дециметры в Дюймы", 'slug': "dm_inch", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Дециметры в Футы", 'slug': "dm_ft", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Дециметры в Ярды", 'slug': "dm_ya", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
#
# insert_to_db(pages, {'name': "Метры в Миллиметры", 'slug': "m_mm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Метры в Сантиметры", 'slug': "m_cm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Метры в Дециметры", 'slug': "m_dm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Метры в Километры", 'slug': "m_km", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Метры в Дюймы", 'slug': "m_inch", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Метры в Ярды", 'slug': "m_ya", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
#
# insert_to_db(pages, {'name': "Километры в Миллиметры", 'slug': "km_mm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Километры в Сантиметры", 'slug': "km_cm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Километры в Дециметры", 'slug': "km_dm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Километры в Метры", 'slug': "km_m", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Километры в Дюймы", 'slug': "km_inch", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Километры в Ярды", 'slug': "km_ya", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
#
# insert_to_db(pages, {'name': "Дюймы в Миллиметры", 'slug': "inch_mm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Дюймы в Сантиметры", 'slug': "inch_cm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Дюймы в Дециметры", 'slug': "inch_dm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Дюймы в Метры", 'slug': "inch_m", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Дюймы в Километры", 'slug': "inch_km", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Дюймы в Футы", 'slug': "inch_ft", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Дюймы в Ярды", 'slug': "inch_ya", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
#
# insert_to_db(pages, {'name': "Футы в Миллиметры", 'slug': "ft_mm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Футы в Сантиметры", 'slug': "ft_cm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Футы в Дециметры", 'slug': "ft_dm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Футы в Метры", 'slug': "ft_m", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Футы в Километры", 'slug': "ft_km", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Футы в Дюймы", 'slug': "ft_inch", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Футы в Ярды", 'slug': "ft_ya", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
#
#
# insert_to_db(pages, {'name': "Ярды в Миллиметры", 'slug': "ya_mm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Ярды в Сантиметры", 'slug': "ya_cm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Ярды в Дециметры", 'slug': "ya_dm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Ярды в Метры", 'slug': "ya_m", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Ярды в Километры", 'slug': "ya_km", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Ярды в Дюймы", 'slug': "ya_inch", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Ярды в Футы", 'slug': "ya_ft", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
#
# insert_to_db(pages, {'name': "Мили в Миллиметры", 'slug': "ml_mm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Мили в Сантиметры", 'slug': "ml_cm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Мили в Дециметры", 'slug': "ml_dm", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Мили в Метры", 'slug': "ml_m", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Мили в Километры", 'slug': "ml_km", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Мили в Дюймы", 'slug': "ml_inch", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Мили в Футы", 'slug': "ml_ft", 'category': 32, 'image': IMAGE_FOLDER + 'distance_i.png'})
#
# insert_to_db(pages, {'name': "Сантиметры² в дециметры²", 'slug': "cm2_dm2", 'category': 33, 'image': IMAGE_FOLDER + 'square_i.png'})
# insert_to_db(pages, {'name': "Сантиметры² в метры²", 'slug': "cm2_m2", 'category': 33, 'image': IMAGE_FOLDER + 'square_i.png'})
# insert_to_db(pages, {'name': "Сантиметры² в километры²", 'slug': "cm2_km2", 'category': 33, 'image': IMAGE_FOLDER + 'square_i.png'})
# insert_to_db(pages, {'name': "Сантиметры² в дюймы²", 'slug': "cm2_inch2", 'category': 33, 'image': IMAGE_FOLDER + 'square_i.png'})
# insert_to_db(pages, {'name': "Сантиметры² в футы²", 'slug': "cm2_ft2", 'category': 33, 'image': IMAGE_FOLDER + 'square_i.png'})
# insert_to_db(pages, {'name': "Сантиметры² в гектары", 'slug': "cm2_ga2", 'category': 33, 'image': IMAGE_FOLDER + 'square_i.png'})
# insert_to_db(pages, {'name': "Сантиметры² в акры", 'slug': "cm2_akr2", 'category': 33, 'image': IMAGE_FOLDER + 'square_i.png'})
#
#
# insert_to_db(pages, {'name': "Метры² в дециметры²", 'slug': "m2_dm2", 'category': 33, 'image': IMAGE_FOLDER + 'square_i.png'})
# insert_to_db(pages, {'name': "Метры² в сантиметры²", 'slug': "m2_cm2", 'category': 33, 'image': IMAGE_FOLDER + 'square_i.png'})
# insert_to_db(pages, {'name': "Метры² в километры²", 'slug': "m2_km2", 'category': 33, 'image': IMAGE_FOLDER + 'square_i.png'})
# insert_to_db(pages, {'name': "Метры² в дюймы²", 'slug': "m2_inch2", 'category': 33, 'image': IMAGE_FOLDER + 'square_i.png'})
# insert_to_db(pages, {'name': "Метры² в футы²", 'slug': "m2_ft2", 'category': 33, 'image': IMAGE_FOLDER + 'square_i.png'})
# insert_to_db(pages, {'name': "Метры² в гектары", 'slug': "m2_ga2", 'category': 33, 'image': IMAGE_FOLDER + 'square_i.png'})
# insert_to_db(pages, {'name': "Метры² в акры", 'slug': "m2_akr2", 'category': 33, 'image': IMAGE_FOLDER + 'square_i.png'})
#
#
# insert_to_db(pages, {'name': "Дециметры² в метры²", 'slug': "dm2_m2", 'category': 33, 'image': IMAGE_FOLDER + 'square_i.png'})
# insert_to_db(pages, {'name': "Дециметры² в сантиметры²", 'slug': "dm2_cm2", 'category': 33, 'image': IMAGE_FOLDER + 'square_i.png'})
# insert_to_db(pages, {'name': "Дециметры² в километры²", 'slug': "dm2_km2", 'category': 33, 'image': IMAGE_FOLDER + 'square_i.png'})
# insert_to_db(pages, {'name': "Дециметры² в дюймы²", 'slug': "dm2_inch2", 'category': 33, 'image': IMAGE_FOLDER + 'square_i.png'})
# insert_to_db(pages, {'name': "Дециметры² в футы²", 'slug': "dm2_ft2", 'category': 33, 'image': IMAGE_FOLDER + 'square_i.png'})
# insert_to_db(pages, {'name': "Дециметры² в гектары", 'slug': "dm2_ga2", 'category': 33, 'image': IMAGE_FOLDER + 'square_i.png'})
# insert_to_db(pages, {'name': "Дециметры² в акры", 'slug': "dm2_akr2", 'category': 33, 'image': IMAGE_FOLDER + 'square_i.png'})
#
# insert_to_db(pages, {'name': "Генератор паролей", 'slug': "password", 'category': 4, 'image': IMAGE_FOLDER + 'pass_i.png'})
# insert_to_db(pages, {'name': "Генератор случайных чисел", 'slug': "random_number", 'category': 4, 'image': IMAGE_FOLDER + 'random_i.png'})


# insert_to_db(pages, {'name': "Pdf в Jpeg", 'slug': "pdf_to_jpeg", 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(pages, {'name': "Pdf в Png", 'slug': "pdf_to_png", 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(pages, {'name': "Pdf в Ico", 'slug': "pdf_to_ico", 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(pages, {'name': "Pdf в Tiff", 'slug': "pdf_to_tiff", 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
#insert_to_db(pages, {'name': "Pdf в WebP", 'slug': "pdf_to_webp", 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})

# insert_to_db(pages, {'name': "Docx в Jpeg", 'slug': "docx_to_jpeg", 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(pages, {'name': "Docx в Png", 'slug': "docx_to_png", 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(pages, {'name': "Docx в Ico", 'slug': "docx_to_ico", 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(pages, {'name': "Docx в Tiff", 'slug': "docx_to_tiff", 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(pages, {'name': "Docx в WebP", 'slug': "docx_to_webp", 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})

# insert_to_db(pages, {'name': "Heic в Jpeg", 'slug': "heic_to_jpeg", 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(pages, {'name': "Heic в Png", 'slug': "heic_to_png", 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
insert_to_db(pages, {'name': "Heic в Ico", 'slug': "heic_to_ico", 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
insert_to_db(pages, {'name': "Heic в Tiff", 'slug': "heic_to_tiff", 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
insert_to_db(pages, {'name': "Heic в WebP", 'slug': "heic_to_webp", 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
