from pydantic import BaseModel


class DistanceModel(BaseModel):
    value: float
    item_change: str
    table: dict = {'mm': 1,
                   'cm': 10,
                   'dm': 100,
                   'm': 1000,
                   'km': 1000000,
                   'inch': 25.4,
                   'ft': 304.8}

    def convert(self):
        new_equal = self.table[self.item_change]
        return self.value * self.equal / new_equal


class Millimeter(DistanceModel):
    equal: float = 1


class Centimeter(DistanceModel):
    equal: float = 10


class Decimeter(DistanceModel):
    equal: float = 100


class Meter(DistanceModel):
    equal: float = 1000


class Kilometer(DistanceModel):
    equal: float = 1000000


class Inch(DistanceModel):
    equal: float = 25.4


class Foot(DistanceModel):
    equal: float = 304.8

