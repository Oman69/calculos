from pydantic import BaseModel


class AreaModel(BaseModel):
    value: float
    item_change: str
    table: dict = {'cm2': 1,
                   'dm2': 100,
                   'inch2': 6.45,
                   'ft2': 929.03,
                   'm2': 10000,
                   'h2': 1_000_000,
                   'akr2': 40_468_600,
                   'ga2': 100_000_000,
                   'km2': 10_000_000_000}

    def convert(self):
        new_equal = self.table[self.item_change]
        return self.value * self.equal / new_equal


class Centimeter(AreaModel):
    equal: float = 1


class Decimeter(AreaModel):
    equal: float = 100


class Meter(AreaModel):
    equal: float = 10000


class Kilometer(AreaModel):
    equal: float = 10_000_000_000


class Inch(AreaModel):
    equal: float = 6.45


class Foot(AreaModel):
    equal: float = 929.03


class Hundred(AreaModel):
    equal: float = 1_000_000


class Akr(AreaModel):
    equal: float = 40_468_600


class Hectare(AreaModel):
    equal: float = 100_000_000
