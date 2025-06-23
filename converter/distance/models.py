from pydantic import BaseModel


class DistanceModel(BaseModel):
    value: float = None
    item_change: str = None
    to_str: str = None
    table: dict = {'mm': 1,
                   'cm': 10,
                   'dm': 100,
                   'm': 1000,
                   'km': 1000000,
                   'in': 25.4,
                   'ft': 304.8,
                   'ya': 914.4,
                   'ml': 1609344}

    def convert(self):
        new_equal = self.table[self.item_change]
        return self.value * self.equal / new_equal

    def view_str(self):
        return self.to_str


class Millimeter(DistanceModel):
    equal: float = 1
    to_str: str = 'Миллиметр'


class Centimeter(DistanceModel):
    equal: float = 10
    to_str: str = 'Сантиметр'


class Decimeter(DistanceModel):
    equal: float = 100
    to_str: str = 'Дециметр'


class Meter(DistanceModel):
    equal: float = 1000
    to_str: str = 'Метр'


class Kilometer(DistanceModel):
    equal: float = 1000000
    to_str: str = 'Километр'


class Inch(DistanceModel):
    equal: float = 25.4
    to_str: str = 'Дюйм'


class Foot(DistanceModel):
    equal: float = 304.8
    to_str: str = 'Фут'


class Yard(DistanceModel):
    equal: float = 914.4
    to_str: str = 'Ярд'


class Mile(DistanceModel):
    equal: float = 1609344
    to_str: str = 'Миля'
