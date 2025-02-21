import math
from pydantic import BaseModel


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