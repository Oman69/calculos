import math
from pydantic import BaseModel


class Gram(BaseModel):
    value: float

    def to_kilogram(self):
        return self.value / 1000

