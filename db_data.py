from sqlalchemy import insert
from db_structure import pages, engine, converter_pages

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
# insert_to_db(converter_pages, {'name': "Граммы в Килограммы", 'ff': "g", 'tf': 'kg', 'category': 31, 'image': IMAGE_FOLDER + 'g_kg.png'})
# insert_to_db(converter_pages, {'name': "Граммы в Милиграммы", 'ff': "g", 'tf': 'mg', 'category': 31, 'image': IMAGE_FOLDER + 'g_kg.png'})
# insert_to_db(converter_pages, {'name': "Граммы в Микрограммы", 'ff': "g", 'tf': 'mkg', 'category': 31, 'image': IMAGE_FOLDER + 'g_kg.png'})
# insert_to_db(converter_pages, {'name': "Граммы в Центнеры", 'ff': "g", 'tf': 'c', 'category': 31, 'image': IMAGE_FOLDER + 'g_kg.png'})
# insert_to_db(converter_pages, {'name': "Граммы в Тонны", 'ff': "g", 'tf': 't', 'category': 31, 'image': IMAGE_FOLDER + 'g_kg.png'})
#
# insert_to_db(converter_pages, {'name': "Килограммы в Граммы", 'ff': "kg", 'tf': 'g', 'category': 31, 'image': IMAGE_FOLDER + 'kg_g.png'})
# insert_to_db(converter_pages, {'name': "Килограммы в Милиграммы", 'ff': "kg", 'tf': 'mg', 'category': 31, 'image': IMAGE_FOLDER + 'kg_mg.png'})
# insert_to_db(converter_pages, {'name': "Килограммы в Микрограммы", 'ff': "kg", 'tf': 'mkg',  'category': 31, 'image': IMAGE_FOLDER + 'kg_mkg.png'})
# insert_to_db(converter_pages, {'name': "Килограммы в Центнеры", 'ff': "kg", 'tf': 'c', 'category': 31, 'image': IMAGE_FOLDER + 'kg_c.png'})
# insert_to_db(converter_pages, {'name': "Килограммы в Тонны", 'ff': "kg", 'tf': 't', 'category': 31, 'image': IMAGE_FOLDER + 'kg_t.png'})
#
# insert_to_db(converter_pages, {'name': "Милиграммы в Граммы", 'ff': "mg", 'tf': 'g', 'category': 31, 'image': IMAGE_FOLDER + 'mg_g.png'})
# insert_to_db(converter_pages, {'name': "Милиграммы в Килограммы", 'ff': "mg", 'tf': 'kg', 'category': 31, 'image': IMAGE_FOLDER + 'mg_kg.png'})
# insert_to_db(converter_pages, {'name': "Милиграммы в Микрограммы", 'ff': "mg", 'tf': 'mkg', 'category': 31, 'image': IMAGE_FOLDER + 'mg_mkg.png'})
# insert_to_db(converter_pages, {'name': "Милиграммы в Центнеры", 'ff': "mg", 'tf': 'c', 'category': 31, 'image': IMAGE_FOLDER + 'mg_c.png'})
# insert_to_db(converter_pages, {'name': "Милиграммы в Тонны", 'ff': "mg", 'tf': 't', 'category': 31, 'image': IMAGE_FOLDER + 'mg_t.png'})
#
# insert_to_db(converter_pages, {'name': "Микрограммы в Граммы", 'ff': "mkg", 'tf': 'g', 'category': 31, 'image': IMAGE_FOLDER + 'mkg_g.png'})
# insert_to_db(converter_pages, {'name': "Микрограммы в Килограммы",  'ff': "mkg", 'tf': 'kg', 'category': 31, 'image': IMAGE_FOLDER + 'mkg_kg.png'})
# insert_to_db(converter_pages, {'name': "Микрограммы в Милиграммы",  'ff': "mkg", 'tf': 'mg', 'category': 31, 'image': IMAGE_FOLDER + 'mkg_mg.png'})
# insert_to_db(converter_pages, {'name': "Микрограммы в Центнеры",  'ff': "mkg", 'tf': 'c', 'category': 31, 'image': IMAGE_FOLDER + 'mkg_c.png'})
# insert_to_db(converter_pages, {'name': "Микрограммы в Тонны",  'ff': "mkg", 'tf': 't', 'category': 31, 'image': IMAGE_FOLDER + 'mkg_t.png'})
#
# insert_to_db(converter_pages, {'name': "Центнеры в Граммы", 'ff': "c", 'tf': 'g', 'category': 31, 'image': IMAGE_FOLDER + 'c_g.png'})
# insert_to_db(converter_pages, {'name': "Центнеры в Килограммы", 'ff': "c", 'tf': 'kg', 'category': 31, 'image': IMAGE_FOLDER + 'c_kg.png'})
# insert_to_db(converter_pages, {'name': "Центнеры в Милиграммы", 'ff': "c", 'tf': 'mg', 'category': 31, 'image': IMAGE_FOLDER + 'c_mg.png'})
# insert_to_db(converter_pages, {'name': "Центнеры в Микрограммы", 'ff': "c", 'tf': 'mkg', 'category': 31, 'image': IMAGE_FOLDER + 'c_mkg.png'})
# insert_to_db(converter_pages, {'name': "Центнеры в Тонны", 'ff': "c", 'tf': 't', 'category': 31, 'image': IMAGE_FOLDER + 'c_t.png'})
# #
# insert_to_db(converter_pages, {'name': "Тонны в Граммы", 'ff': "t", 'tf': 'g', 'category': 31, 'image': IMAGE_FOLDER + 't_g.png'})
# insert_to_db(converter_pages, {'name': "Тонны в Килограммы", 'ff': "t", 'tf': 'kg', 'category': 31, 'image': IMAGE_FOLDER + 't_kg.png'})
# insert_to_db(converter_pages, {'name': "Тонны в Милиграммы", 'ff': "t", 'tf': 'mg', 'category': 31, 'image': IMAGE_FOLDER + 't_mg.png'})
# insert_to_db(converter_pages, {'name': "Тонны в Микрограммы", 'ff': "t", 'tf': 'mkg', 'category': 31, 'image': IMAGE_FOLDER + 't_mkg.png'})
# insert_to_db(converter_pages, {'name': "Тонны в Центнеры", 'ff': "t", 'tf': 'c', 'category': 31, 'image': IMAGE_FOLDER + 't_c.png'})
#
insert_to_db(converter_pages, {'name': "Миллиметры в Сантиметры", 'ff': "mm", 'tf': 'cm', 'category': 32, 'image': IMAGE_FOLDER + 'mm_cm.png'})
insert_to_db(converter_pages, {'name': "Миллиметры в Дециметры", 'ff': "mm", 'tf': 'dm',  'category': 32, 'image': IMAGE_FOLDER + 'mm_dm.png'})
insert_to_db(converter_pages, {'name': "Миллиметры в Метры", 'ff': "mm", 'tf': 'm', 'category': 32, 'image': IMAGE_FOLDER + 'mm_m.png'})
insert_to_db(converter_pages, {'name': "Миллиметры в Километры", 'ff': "mm", 'tf': 'km',  'category': 32, 'image': IMAGE_FOLDER + 'mm_km.png'})
insert_to_db(converter_pages, {'name': "Миллиметры в Дюймы", 'ff': "mm", 'tf': 'in',  'category': 32, 'image': IMAGE_FOLDER + 'mm_in.png'})
insert_to_db(converter_pages, {'name': "Миллиметры в Футы", 'ff': "mm", 'tf': 'ft',  'category': 32, 'image': IMAGE_FOLDER + 'mm_ft.png'})
insert_to_db(converter_pages, {'name': "Миллиметры в Ярды", 'ff': "mm", 'tf': 'ya',  'category': 32, 'image': IMAGE_FOLDER + 'mm_ya.png'})
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


# insert_to_db(converter_pages, {'name': "Pdf в Jpeg", 'ff': "pdf", 'tf': 'jpeg', 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(converter_pages, {'name': "Pdf в Png", 'ff': "pdf", 'tf': 'png', 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(converter_pages, {'name': "Pdf в Ico", 'ff': "pdf", 'tf': 'ico', 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(converter_pages, {'name': "Pdf в Tiff", 'ff': "pdf", 'tf': 'tiff', 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(converter_pages, {'name': "Pdf в WebP", 'ff': "pdf", 'tf': 'webp', 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})

# insert_to_db(converter_pages, {'name': "Docx в Jpeg", 'ff': "docx", 'tf': 'jpeg', 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(converter_pages, {'name': "Docx в Png", 'ff': "docx", 'tf': 'png', 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(converter_pages, {'name': "Docx в Ico", 'ff': "docx", 'tf': 'ico', 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(converter_pages, {'name': "Docx в Tiff", 'ff': "docx", 'tf': 'tiff', 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(converter_pages, {'name': "Docx в WebP", 'ff': "docx", 'tf': 'webp', 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
#
# insert_to_db(converter_pages, {'name': "Heic в Jpeg", 'ff': "heic", 'tf': 'jpeg', 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(converter_pages, {'name': "Heic в Png",  'ff': "heic", 'tf': 'png', 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(converter_pages, {'name': "Heic в Ico",  'ff': "heic", 'tf': 'ico', 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(converter_pages, {'name': "Heic в Tiff",  'ff': "heic", 'tf': 'tiff', 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(converter_pages, {'name': "Heic в WebP",  'ff': "heic", 'tf': 'webp', 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(converter_pages, {'name': "Heic в Pdf", 'ff': "heic", 'tf': 'pdf', 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
#
# insert_to_db(converter_pages, {'name': "Jpeg в Pdf", 'ff': "jpeg", 'tf': 'pdf', 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(converter_pages, {'name': "Jpeg в Png", 'ff': "jpeg", 'tf': 'png', 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(converter_pages, {'name': "Jpeg в Webp", 'ff': "jpeg", 'tf': 'webp', 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(converter_pages, {'name': "Jpeg в Ico", 'ff': "jpeg", 'tf': 'ico', 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(converter_pages, {'name': "Jpeg в Tiff", 'ff': "jpeg", 'tf': 'tiff', 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
#
# insert_to_db(converter_pages, {'name': "Png в Pdf", 'ff': "png", 'tf': 'pdf', 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(converter_pages, {'name': "Png в Jpeg", 'ff': "png", 'tf': 'jpeg', 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(converter_pages, {'name': "Png в Webp", 'ff': "png", 'tf': 'webp', 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(converter_pages, {'name': "Png в Ico", 'ff': "png", 'tf': 'ico', 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
# insert_to_db(converter_pages, {'name': "Png в Tiff", 'ff': "png", 'tf': 'tiff', 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})

# insert_to_db(converter_pages, {'name': "Webp в Pdf", 'slug': "webp_to_pdf", 'category': 5, 'image': IMAGE_FOLDER + 'random_i.png'})
