import math
from pydantic import BaseModel, Field, ValidationError
from typing_extensions import Annotated


class Circle(BaseModel):
    radius: Annotated[str, Field(description="Радиус окружности", min_length=1)]


    def get_area(self):
        return round(math.pi * float(self.radius) ** 2, 2)

    def get_length(self):
        return round(math.pi * float(self.radius) * 2, 2)


class Rectangle(BaseModel):
    a: str
    b: str

    def get_area(self):
        return float(self.a) * float(self.b)

    def get_perimeter(self):
        return (float(self.a) + float(self.b)) * 2


class Square(BaseModel):
    a: str

    def get_area(self):
        return float(self.a) ** 2

    def get_perimeter(self):
        return float(self.a) * 4


class RightTriangle(BaseModel):
    a: str
    b: str

    def get_area(self):
        return (float(self.a) * float(self.b)) * 0.5

    def get_hypotenuse(self):
        return math.sqrt(float(self.a)**2 + float(self.b)**2)


class IsoscelesTriangle(BaseModel):
    h: str
    c: str

    def get_area(self):
        return (float(self.h) * float(self.c)) * 0.5


class EquTriangle(BaseModel):
    h: str
    c: str

    def get_area(self):
        return (float(self.h) * float(self.c)) * 0.5

class Rhombus(BaseModel):
    a: str
    h: str = None

    def get_area(self):
        return float(self.a) * float(self.h)

    def get_perimeter(self):
        return float(self.a) * 4
