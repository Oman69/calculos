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

# insert_to_db(pages, {'name': "Генератор паролей", 'slug': "password", 'category': 4, 'image': IMAGE_FOLDER + 'pass_i.png'})
# insert_to_db(pages, {'name': "Генератор случайных чисел", 'slug': "random_number", 'category': 4, 'image': IMAGE_FOLDER + 'random_i.png'})

#
# insert_to_db(pages, {'name': "Вес и масса", 'slug': "weight", 'category': 3, 'image': IMAGE_FOLDER + 'weight_i.png'})
# insert_to_db(pages, {'name': "Расстояние и длина", 'slug': "distance", 'category': 3, 'image': IMAGE_FOLDER + 'distance_i.png'})
# insert_to_db(pages, {'name': "Площадь", 'slug': "area", 'category': 3, 'image': IMAGE_FOLDER + 'square_i.png'})
#insert_to_db(pages, {'name': "Конвертеры файлов", 'slug': "files_converter", 'category': 3, 'image': IMAGE_FOLDER + 'file_i.png'})
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
# insert_to_db(converter_pages, {'name': "Миллиметры в Сантиметры", 'ff': "mm", 'tf': 'cm', 'category': 32, 'image': IMAGE_FOLDER + 'mm_cm.png'})
# insert_to_db(converter_pages, {'name': "Миллиметры в Дециметры", 'ff': "mm", 'tf': 'dm',  'category': 32, 'image': IMAGE_FOLDER + 'mm_dm.png'})
# insert_to_db(converter_pages, {'name': "Миллиметры в Метры", 'ff': "mm", 'tf': 'm', 'category': 32, 'image': IMAGE_FOLDER + 'mm_m.png'})
# insert_to_db(converter_pages, {'name': "Миллиметры в Километры", 'ff': "mm", 'tf': 'km',  'category': 32, 'image': IMAGE_FOLDER + 'mm_km.png'})
# insert_to_db(converter_pages, {'name': "Миллиметры в Дюймы", 'ff': "mm", 'tf': 'in',  'category': 32, 'image': IMAGE_FOLDER + 'mm_in.png'})
# insert_to_db(converter_pages, {'name': "Миллиметры в Футы", 'ff': "mm", 'tf': 'ft',  'category': 32, 'image': IMAGE_FOLDER + 'mm_ft.png'})
# insert_to_db(converter_pages, {'name': "Миллиметры в Ярды", 'ff': "mm", 'tf': 'ya',  'category': 32, 'image': IMAGE_FOLDER + 'mm_ya.png'})
#
# insert_to_db(converter_pages, {'name': "Сантиметры в Миллиметры", 'ff': "cm", 'tf': 'mm', 'category': 32, 'image': IMAGE_FOLDER + 'cm_mm.png'})
# insert_to_db(converter_pages, {'name': "Сантиметры в Дециметры", 'ff': "cm", 'tf': 'dm', 'category': 32, 'image': IMAGE_FOLDER + 'cm_dm.png'})
# insert_to_db(converter_pages, {'name': "Сантиметры в Метры", 'ff': "cm", 'tf': 'm', 'category': 32, 'image': IMAGE_FOLDER + 'cm_m.png'})
# insert_to_db(converter_pages, {'name': "Сантиметры в Километры", 'ff': "cm", 'tf': 'km', 'category': 32, 'image': IMAGE_FOLDER + 'cm_km.png'})
# insert_to_db(converter_pages, {'name': "Сантиметры в Дюймы", 'ff': "cm", 'tf': 'in', 'category': 32, 'image': IMAGE_FOLDER + 'cm_in.png'})
# insert_to_db(converter_pages, {'name': "Сантиметры в Футы", 'ff': "cm", 'tf': 'ft', 'category': 32, 'image': IMAGE_FOLDER + 'cm_ft.png'})
# insert_to_db(converter_pages, {'name': "Сантиметры в Ярды", 'ff': "cm", 'tf': 'ya', 'category': 32, 'image': IMAGE_FOLDER + 'cm_ya.png'})
#
# insert_to_db(converter_pages, {'name': "Дециметры в Миллиметры", 'ff': "dm", 'tf': 'mm', 'category': 32, 'image': IMAGE_FOLDER + 'dm_mm.png'})
# insert_to_db(converter_pages, {'name': "Дециметры в Сантиметры", 'ff': "dm", 'tf': 'cm', 'category': 32, 'image': IMAGE_FOLDER + 'dm_cm.png'})
# insert_to_db(converter_pages, {'name': "Дециметры в Метры", 'ff': "dm", 'tf': 'm',  'category': 32, 'image': IMAGE_FOLDER + 'dm_m.png'})
# insert_to_db(converter_pages, {'name': "Дециметры в Километры", 'ff': "dm", 'tf': 'km', 'category': 32, 'image': IMAGE_FOLDER + 'dm_km.png'})
# insert_to_db(converter_pages, {'name': "Дециметры в Дюймы", 'ff': "dm", 'tf': 'in',  'category': 32, 'image': IMAGE_FOLDER + 'dm_in.png'})
# insert_to_db(converter_pages, {'name': "Дециметры в Футы", 'ff': "dm", 'tf': 'ft',  'category': 32, 'image': IMAGE_FOLDER + 'dm_ft.png'})
# insert_to_db(converter_pages, {'name': "Дециметры в Ярды", 'ff': "dm", 'tf': 'ya', 'category': 32, 'image': IMAGE_FOLDER + 'dm_ya.png'})
#
# insert_to_db(converter_pages, {'name': "Метры в Миллиметры", 'ff': "m", 'tf': 'mm', 'category': 32, 'image': IMAGE_FOLDER + 'm_mm.png'})
# insert_to_db(converter_pages, {'name': "Метры в Сантиметры", 'ff': "m", 'tf': 'cm', 'category': 32, 'image': IMAGE_FOLDER + 'm_cm.png'})
# insert_to_db(converter_pages, {'name': "Метры в Дециметры", 'ff': "m", 'tf': 'dm', 'category': 32, 'image': IMAGE_FOLDER + 'm_dm.png'})
# insert_to_db(converter_pages, {'name': "Метры в Километры", 'ff': "m", 'tf': 'km', 'category': 32, 'image': IMAGE_FOLDER + 'm_km.png'})
# insert_to_db(converter_pages, {'name': "Метры в Дюймы", 'ff': "m", 'tf': 'in', 'category': 32, 'image': IMAGE_FOLDER + 'm_in.png'})
# insert_to_db(converter_pages, {'name': "Метры в Ярды", 'ff': "m", 'tf': 'ya', 'category': 32, 'image': IMAGE_FOLDER + 'm_ya.png'})
#
# insert_to_db(converter_pages, {'name': "Километры в Миллиметры", 'ff': "km", 'tf': 'mm', 'category': 32, 'image': IMAGE_FOLDER + 'km_mm.png'})
# insert_to_db(converter_pages, {'name': "Километры в Сантиметры", 'ff': "km", 'tf': 'cm',  'category': 32, 'image': IMAGE_FOLDER + 'km_cm.png'})
# insert_to_db(converter_pages, {'name': "Километры в Дециметры",  'ff': "km", 'tf': 'dm', 'category': 32, 'image': IMAGE_FOLDER + 'km_dm.png'})
# insert_to_db(converter_pages, {'name': "Километры в Метры", 'ff': "km", 'tf': 'm', 'category': 32, 'image': IMAGE_FOLDER + 'km_m.png'})
# insert_to_db(converter_pages, {'name': "Километры в Дюймы", 'ff': "km", 'tf': 'in', 'category': 32, 'image': IMAGE_FOLDER + 'km_in.png'})
# insert_to_db(converter_pages, {'name': "Километры в Ярды", 'ff': "km", 'tf': 'ys', 'category': 32, 'image': IMAGE_FOLDER + 'km_ya.png'})
#
# insert_to_db(converter_pages, {'name': "Дюймы в Миллиметры", 'ff': "in", 'tf': 'mm', 'category': 32, 'image': IMAGE_FOLDER + 'in_mm.png'})
# insert_to_db(converter_pages, {'name': "Дюймы в Сантиметры", 'ff': "in", 'tf': 'cm','category': 32, 'image': IMAGE_FOLDER + 'in_cm.png'})
# insert_to_db(converter_pages, {'name': "Дюймы в Дециметры", 'ff': "in", 'tf': 'dm', 'category': 32, 'image': IMAGE_FOLDER + 'in_dm.png'})
# insert_to_db(converter_pages, {'name': "Дюймы в Метры", 'ff': "in", 'tf': 'm', 'category': 32, 'image': IMAGE_FOLDER + 'in_m.png'})
# insert_to_db(converter_pages, {'name': "Дюймы в Километры", 'ff': "in", 'tf': 'km', 'category': 32, 'image': IMAGE_FOLDER + 'in_km.png'})
# insert_to_db(converter_pages, {'name': "Дюймы в Футы", 'ff': "in", 'tf': 'ft', 'category': 32, 'image': IMAGE_FOLDER + 'in_ft.png'})
# insert_to_db(converter_pages, {'name': "Дюймы в Ярды", 'ff': "in", 'tf': 'ya', 'category': 32, 'image': IMAGE_FOLDER + 'in_ya.png'})
#
# insert_to_db(converter_pages, {'name': "Футы в Миллиметры", 'ff': "ft", 'tf': 'mm', 'category': 32, 'image': IMAGE_FOLDER + 'ft_mm.png'})
# insert_to_db(converter_pages, {'name': "Футы в Сантиметры", 'ff': "ft", 'tf': 'cm', 'category': 32, 'image': IMAGE_FOLDER + 'ft_cm.png'})
# insert_to_db(converter_pages, {'name': "Футы в Дециметры", 'ff': "ft", 'tf': 'dm', 'category': 32, 'image': IMAGE_FOLDER + 'ft_dm.png'})
# insert_to_db(converter_pages, {'name': "Футы в Метры", 'ff': "ft", 'tf': 'm', 'category': 32, 'image': IMAGE_FOLDER + 'ft_m.png'})
# insert_to_db(converter_pages, {'name': "Футы в Километры", 'ff': "ft", 'tf': 'km', 'category': 32, 'image': IMAGE_FOLDER + 'ft_km.png'})
# insert_to_db(converter_pages, {'name': "Футы в Дюймы", 'ff': "ft", 'tf': 'in', 'category': 32, 'image': IMAGE_FOLDER + 'ft_in.png'})
# insert_to_db(converter_pages, {'name': "Футы в Ярды", 'ff': "ft", 'tf': 'ya', 'category': 32, 'image': IMAGE_FOLDER + 'ft_ya.png'})
#
#
# insert_to_db(converter_pages, {'name': "Ярды в Миллиметры", 'ff': "ya", 'tf': 'mm', 'category': 32, 'image': IMAGE_FOLDER + 'ya_mm.png'})
# insert_to_db(converter_pages, {'name': "Ярды в Сантиметры", 'ff': "ya", 'tf': 'cm',  'category': 32, 'image': IMAGE_FOLDER + 'ya_cm.png'})
# insert_to_db(converter_pages, {'name': "Ярды в Дециметры", 'ff': "ya", 'tf': 'dm',  'category': 32, 'image': IMAGE_FOLDER + 'ya_dm.png'})
# insert_to_db(converter_pages, {'name': "Ярды в Метры", 'ff': "ya", 'tf': 'm',  'category': 32, 'image': IMAGE_FOLDER + 'ya_m.png'})
# insert_to_db(converter_pages, {'name': "Ярды в Километры", 'ff': "ya", 'tf': 'km',  'category': 32, 'image': IMAGE_FOLDER + 'ya_km.png'})
# insert_to_db(converter_pages, {'name': "Ярды в Дюймы", 'ff': "ya", 'tf': 'in',  'category': 32, 'image': IMAGE_FOLDER + 'ya_in.png'})
# insert_to_db(converter_pages, {'name': "Ярды в Футы", 'ff': "ya", 'tf': 'ft',  'category': 32, 'image': IMAGE_FOLDER + 'ya_ft.png'})
#
insert_to_db(converter_pages, {'name': "Сантиметры² в дециметры²", 'ff': "cm", 'tf': 'dm', 'category': 33, 'image': IMAGE_FOLDER + 'cm_dm.png'})
insert_to_db(converter_pages, {'name': "Сантиметры² в метры²", 'ff': "cm", 'tf': 'm', 'category': 33, 'image': IMAGE_FOLDER + 'cm_m.png'})
insert_to_db(converter_pages, {'name': "Сантиметры² в километры²", 'ff': "cm", 'tf': 'km', 'category': 33, 'image': IMAGE_FOLDER + 'cm_km.png'})
insert_to_db(converter_pages, {'name': "Сантиметры² в дюймы²", 'ff': "cm", 'tf': 'in', 'category': 33, 'image': IMAGE_FOLDER + 'cm_in.png'})
insert_to_db(converter_pages, {'name': "Сантиметры² в футы²", 'ff': "cm", 'tf': 'ft', 'category': 33, 'image': IMAGE_FOLDER + 'cm_ft.png'})
insert_to_db(converter_pages, {'name': "Сантиметры² в гектары", 'ff': "cm", 'tf': 'ga', 'category': 33, 'image': IMAGE_FOLDER + 'cm_ga.png'})
insert_to_db(converter_pages, {'name': "Сантиметры² в акры", 'ff': "cm", 'tf': 'akr', 'category': 33, 'image': IMAGE_FOLDER + 'cm_akr.png'})


insert_to_db(converter_pages, {'name': "Метры² в дециметры²", 'ff': "m", 'tf': 'dm', 'category': 33, 'image': IMAGE_FOLDER + 'm_dm.png'})
insert_to_db(converter_pages, {'name': "Метры² в сантиметры²", 'ff': "m", 'tf': 'cm', 'category': 33, 'image': IMAGE_FOLDER + 'm_cm.png'})
insert_to_db(converter_pages, {'name': "Метры² в километры²", 'ff': "m", 'tf': 'km', 'category': 33, 'image': IMAGE_FOLDER + 'm_km.png'})
insert_to_db(converter_pages, {'name': "Метры² в дюймы²", 'ff': "m", 'tf': 'in', 'category': 33, 'image': IMAGE_FOLDER + 'm_in.png'})
insert_to_db(converter_pages, {'name': "Метры² в футы²", 'ff': "m", 'tf': 'ft', 'category': 33, 'image': IMAGE_FOLDER + 'm_ft.png'})
insert_to_db(converter_pages, {'name': "Метры² в гектары", 'ff': "m", 'tf': 'ga', 'category': 33, 'image': IMAGE_FOLDER + 'm_ga.png'})
insert_to_db(converter_pages, {'name': "Метры² в акры", 'ff': "m", 'tf': 'akr', 'category': 33, 'image': IMAGE_FOLDER + 'm_akr.png'})


insert_to_db(converter_pages, {'name': "Дециметры² в метры²", 'ff': "dm", 'tf': 'm', 'category': 33, 'image': IMAGE_FOLDER + 'dm_m.png'})
insert_to_db(converter_pages, {'name': "Дециметры² в сантиметры²", 'ff': "dm", 'tf': 'cm',  'category': 33, 'image': IMAGE_FOLDER + 'dm_cm.png'})
insert_to_db(converter_pages, {'name': "Дециметры² в километры²", 'ff': "dm", 'tf': 'km',  'category': 33, 'image': IMAGE_FOLDER + 'dm_km.png'})
insert_to_db(converter_pages, {'name': "Дециметры² в дюймы²", 'ff': "dm", 'tf': 'in', 'category': 33, 'image': IMAGE_FOLDER + 'dm_in.png'})
insert_to_db(converter_pages, {'name': "Дециметры² в футы²", 'ff': "dm", 'tf': 'ft', 'category': 33, 'image': IMAGE_FOLDER + 'dm_ft.png'})
insert_to_db(converter_pages, {'name': "Дециметры² в гектары", 'ff': "dm", 'tf': 'ga', 'category': 33, 'image': IMAGE_FOLDER + 'dm_ga.png'})
insert_to_db(converter_pages, {'name': "Дециметры² в акры", 'ff': "dm", 'tf': 'akr', 'category': 33, 'image': IMAGE_FOLDER + 'dm_akr.png'})


insert_to_db(converter_pages, {'name': "Километры² в метры²", 'ff': "km", 'tf': 'm', 'category': 33, 'image': IMAGE_FOLDER + 'km_m.png'})
insert_to_db(converter_pages, {'name': "Километры² в сантиметры²", 'ff': "km", 'tf': 'cm',  'category': 33, 'image': IMAGE_FOLDER + 'km_cm.png'})
insert_to_db(converter_pages, {'name': "Километры² в дециметры²", 'ff': "km", 'tf': 'dm',  'category': 33, 'image': IMAGE_FOLDER + 'km_dm.png'})
insert_to_db(converter_pages, {'name': "Километры² в дюймы²", 'ff': "km", 'tf': 'in', 'category': 33, 'image': IMAGE_FOLDER + 'km_in.png'})
insert_to_db(converter_pages, {'name': "Километры² в футы²", 'ff': "km", 'tf': 'ft', 'category': 33, 'image': IMAGE_FOLDER + 'km_ft.png'})
insert_to_db(converter_pages, {'name': "Километры² в гектары", 'ff': "km", 'tf': 'ga', 'category': 33, 'image': IMAGE_FOLDER + 'km_ga.png'})
insert_to_db(converter_pages, {'name': "Километры² в акры", 'ff': "km", 'tf': 'akr', 'category': 33, 'image': IMAGE_FOLDER + 'km_akr.png'})


insert_to_db(converter_pages, {'name': "Дюймы² в метры²", 'ff': "in", 'tf': 'm', 'category': 33, 'image': IMAGE_FOLDER + 'in_m.png'})
insert_to_db(converter_pages, {'name': "Дюймы² в сантиметры²", 'ff': "in", 'tf': 'cm',  'category': 33, 'image': IMAGE_FOLDER + 'in_cm.png'})
insert_to_db(converter_pages, {'name': "Дюймы² в дециметры²", 'ff': "in", 'tf': 'dm',  'category': 33, 'image': IMAGE_FOLDER + 'in_dm.png'})
insert_to_db(converter_pages, {'name': "Дюймы² в километры²", 'ff': "in", 'tf': 'km', 'category': 33, 'image': IMAGE_FOLDER + 'in_km.png'})
insert_to_db(converter_pages, {'name': "Дюймы² в футы²", 'ff': "in", 'tf': 'ft', 'category': 33, 'image': IMAGE_FOLDER + 'in_ft.png'})
insert_to_db(converter_pages, {'name': "Дюймы² в гектары", 'ff': "in", 'tf': 'ga', 'category': 33, 'image': IMAGE_FOLDER + 'in_ga.png'})
insert_to_db(converter_pages, {'name': "Дюймы² в акры", 'ff': "in", 'tf': 'akr', 'category': 33, 'image': IMAGE_FOLDER + 'in_akr.png'})


insert_to_db(converter_pages, {'name': "Футы² в метры²", 'ff': "ft", 'tf': 'm', 'category': 33, 'image': IMAGE_FOLDER + 'ft_m.png'})
insert_to_db(converter_pages, {'name': "Футы² в сантиметры²", 'ff': "ft", 'tf': 'cm',  'category': 33, 'image': IMAGE_FOLDER + 'ft_cm.png'})
insert_to_db(converter_pages, {'name': "Футы² в дециметры²", 'ff': "ft", 'tf': 'dm',  'category': 33, 'image': IMAGE_FOLDER + 'ft_dm.png'})
insert_to_db(converter_pages, {'name': "Футы² в километры²", 'ff': "ft", 'tf': 'km', 'category': 33, 'image': IMAGE_FOLDER + 'ft_km.png'})
insert_to_db(converter_pages, {'name': "Футы² в дюймы²", 'ff': "ft", 'tf': 'in', 'category': 33, 'image': IMAGE_FOLDER + 'ft_in.png'})
insert_to_db(converter_pages, {'name': "Футы² в гектары", 'ff': "ft", 'tf': 'ga', 'category': 33, 'image': IMAGE_FOLDER + 'ft_ga.png'})
insert_to_db(converter_pages, {'name': "Футы² в акры", 'ff': "ft", 'tf': 'akr', 'category': 33, 'image': IMAGE_FOLDER + 'ft_akr.png'})

insert_to_db(converter_pages, {'name': "Гектары в метры²", 'ff': "ga", 'tf': 'm', 'category': 33, 'image': IMAGE_FOLDER + 'ga_m.png'})
insert_to_db(converter_pages, {'name': "Гектары в сантиметры²", 'ff': "ga", 'tf': 'cm',  'category': 33, 'image': IMAGE_FOLDER + 'ga_cm.png'})
insert_to_db(converter_pages, {'name': "Гектары в дециметры²", 'ff': "ga", 'tf': 'dm',  'category': 33, 'image': IMAGE_FOLDER + 'ga_dm.png'})
insert_to_db(converter_pages, {'name': "Гектары в километры²", 'ff': "ga", 'tf': 'km', 'category': 33, 'image': IMAGE_FOLDER + 'ga_km.png'})
insert_to_db(converter_pages, {'name': "Гектары в дюймы²", 'ff': "ga", 'tf': 'in', 'category': 33, 'image': IMAGE_FOLDER + 'ga_in.png'})
insert_to_db(converter_pages, {'name': "Гектары в футы", 'ff': "ga", 'tf': 'ft', 'category': 33, 'image': IMAGE_FOLDER + 'ga_ft.png'})
insert_to_db(converter_pages, {'name': "Гектары в акры", 'ff': "ga", 'tf': 'akr', 'category': 33, 'image': IMAGE_FOLDER + 'ga_akr.png'})

insert_to_db(converter_pages, {'name': "Акры в метры²", 'ff': "akr", 'tf': 'm', 'category': 33, 'image': IMAGE_FOLDER + 'akr_m.png'})
insert_to_db(converter_pages, {'name': "Акры в сантиметры²", 'ff': "akr", 'tf': 'cm',  'category': 33, 'image': IMAGE_FOLDER + 'akr_cm.png'})
insert_to_db(converter_pages, {'name': "Акры в дециметры²", 'ff': "akr", 'tf': 'dm',  'category': 33, 'image': IMAGE_FOLDER + 'akr_dm.png'})
insert_to_db(converter_pages, {'name': "Акры в километры²", 'ff': "akr", 'tf': 'km', 'category': 33, 'image': IMAGE_FOLDER + 'akr_km.png'})
insert_to_db(converter_pages, {'name': "Акры в дюймы²", 'ff': "akr", 'tf': 'in', 'category': 33, 'image': IMAGE_FOLDER + 'akr_in.png'})
insert_to_db(converter_pages, {'name': "Акры в футы", 'ff': "akr", 'tf': 'ft', 'category': 33, 'image': IMAGE_FOLDER + 'akr_ft.png'})
insert_to_db(converter_pages, {'name': "Акры в гектары", 'ff': "akr", 'tf': 'ga', 'category': 33, 'image': IMAGE_FOLDER + 'akr_ga.png'})

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
