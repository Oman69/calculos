from pydantic import BaseModel


class AreaModel(BaseModel):
    value: float = None
    item_change: str = None
    to_str: str = None
    table: dict = {'cm': 1,
                   'dm': 100,
                   'in': 6.45,
                   'ft': 929.03,
                   'm': 10000,
                   'akr': 40_468_600,
                   'ga': 100_000_000,
                   'km': 10_000_000_000}

    def convert(self):
        new_equal = self.table[self.item_change]
        return self.value * self.equal / new_equal

    def view_str(self):
        return self.to_str


class Centimeter(AreaModel):
    equal: float = 1
    to_str: str = 'Кв. сантиметр'


class Decimeter(AreaModel):
    equal: float = 100
    to_str: str = 'Кв. дециметр'


class Meter(AreaModel):
    equal: float = 10000
    to_str: str = 'Кв. метр'


class Kilometer(AreaModel):
    equal: float = 10_000_000_000
    to_str: str = 'Кв. километр'


class Inch(AreaModel):
    equal: float = 6.45
    to_str: str = 'Кв. дюйм'


class Foot(AreaModel):
    equal: float = 929.03
    to_str: str = 'Кв. фут'


class Akr(AreaModel):
    equal: float = 40_468_600
    to_str: str = 'Акр'


class Hectare(AreaModel):
    equal: float = 100_000_000
    to_str: str = 'Гектар'
