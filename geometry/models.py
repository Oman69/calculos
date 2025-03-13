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
    a: str = None
    c: str
    h: str = None

    def get_area(self):
        return (float(self.h) * float(self.c)) * 0.5

    def get_height(self):
        return math.sqrt(float(self.a)**2 - (float(self.c)**2)/4)


class EquTriangle(BaseModel):
    a: int

    def get_area(self):
        return (self.a**2 * math.sqrt(3)) / 4

    def get_height(self):
        return self.a * math.sqrt(3) * 0.5


class Rhombus(BaseModel):
    a: int
    h: int = None

    def get_area(self):
        return self.a * self.h

    def get_perimeter(self):
        return self.a * 4


class Trap(BaseModel):
    a: int
    b: int
    h: int = None

    def get_area(self):
        return (self.a + self.b) * 0.5 * self.h

    def get_perimeter(self):
        return float(self.a) * 4
