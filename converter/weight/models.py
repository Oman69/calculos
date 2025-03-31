from pydantic import BaseModel


class WeightModel(BaseModel):
    value: float
    item_change: str

    def convert(self):
        pass


class Gram(WeightModel):

    def convert(self):
        operations = {
            'kg': self.value / 1000,
            'mg': self.value * 1000,
            'mkg': self.value * 1_000_000,
            'c': self.value / 100_000,
            't': self.value / 1_000_000,
        }

        return operations[self.item_change]


class Kilogram(BaseModel):
    value: float

    def to_g(self):
        return self.value * 1000

    def to_mg(self):
        return self.value * 1_000_000

    def to_mkg(self):
        return self.value * 1_000_000_000

    def to_c(self):
        return self.value / 100

    def to_t(self):
        return self.value / 1_000


class Centner(BaseModel):
    value: float

    def to_g(self):
        return self.value * 100_000

    def to_mg(self):
        return self.value * 100_000_000

    def to_mkg(self):
        return self.value * 100_000_000_000

    def to_kg(self):
        return self.value * 100

    def to_t(self):
        return self.value / 10


