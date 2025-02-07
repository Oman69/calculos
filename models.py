import math
from typing import Union
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


class Circle(BaseModel):
    radius: str

    def get_area(self):
        return round(math.pi * float(self.radius) ** 2, 2)

    def get_length(self):
        return round(math.pi * float(self.radius) * 2, 2)


class Rectangle(BaseModel):
    a: str
    b: str

    def get_area(self):
        return round(float(self.a) * float(self.b), 2)

    def get_perimeter(self):
        return round(float(self.a) + float(self.b) * 2, 2)