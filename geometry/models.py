import math
from pydantic import BaseModel, Field, ValidationError


class Circle(BaseModel):
    radius: float

    def get_area(self):
        return round(math.pi * self.radius ** 2, 2)

    def get_length(self):
        return round(math.pi * self.radius * 2, 2)


class Rectangle(BaseModel):
    a: float
    b: float

    def get_area(self):
        return self.a * self.b

    def get_perimeter(self):
        return (self.a + self.b) * 2

    def get_diag(self):
        return math.sqrt(self.a**2 + self.b**2)


class Square(BaseModel):
    a: float

    def get_area(self):
        return self.a ** 2

    def get_perimeter(self):
        return self.a * 4

    def get_diag(self):
        return self.a * math.sqrt(2)


class RightTriangle(BaseModel):
    a: float
    b: float

    def get_area(self):
        return self.a * self.b * 0.5

    def get_hypotenuse(self):
        return math.sqrt(self.a**2 + self.b**2)


class IsoTriangle(BaseModel):
    a: float = None
    c: float
    h: float = None

    def get_area(self):
        return self.h * self.c * 0.5

    def get_height(self):
        return math.sqrt(self.a ** 2 - (self.c**2/4))


class EquTriangle(BaseModel):
    a: float

    def get_area(self):
        return (self.a**2 * math.sqrt(3)) / 4

    def get_height(self):
        return self.a * math.sqrt(3) * 0.5


class Rhombus(BaseModel):
    a: float
    h: float = None

    def get_area(self):
        return self.a * self.h

    def get_perimeter(self):
        return self.a * 4


class Trap(BaseModel):
    a: float
    b: float
    c: float = None
    d: float = None
    h: float = None

    def get_area(self):
        return (self.a + self.b) * 0.5 * self.h

    def get_perimeter(self):
        return sum([self.a, self.b, self.c, self.d])


class Cube(BaseModel):
    a: float

    def get_area(self):
        return self.a ** 2 * 6

    def get_volume(self):
        return self.a ** 3