from pydantic import BaseModel


class WeightModel(BaseModel):
    value: float
    item_change: str

    def convert(self):
        return 'Error'


class Gram(WeightModel):

    def convert(self):
        operations = {
            'kg': self.value / 1000,
            'mg': self.value * 1000,
            'mkg': self.value * 1_000_000,
            'c': self.value / 100_000,
            't': self.value / 1_000_000,
            'k': self.value * 5,
            'g': self.value
        }

        return operations[self.item_change]


class Kilogram(WeightModel):

    def convert(self):
        operations = {
            'g': self.value * 1000,
            'mg': self.value * 1_000_000,
            'mkg': self.value * 1_000_000_000,
            'c': self.value / 100,
            't': self.value / 1_000,
            'k': self.value * 5000
        }

        return operations[self.item_change]


class Milligram(WeightModel):

    def convert(self):
        operations = {
            'g': self.value / 1000,
            'kg': self.value / 1_000_000,
            'mkg': self.value * 1_000,
            'c': self.value / 100_000_000,
            't': self.value / 1_000_000_000,
            'k': self.value / 200
        }

        return operations[self.item_change]


class Microgram(WeightModel):

    def convert(self):
        operations = {
            'g': self.value / 1_000_000,
            'kg': self.value / 1_000_000_000,
            'mg': self.value / 1_000,
            'c': self.value / 100_000_000_000,
            't': self.value / 1_000_000_000_000,
            'k': self.value / 200_000
        }

        return operations[self.item_change]


class Centner(WeightModel):

    def convert(self):
        operations = {
            'g': self.value * 100_000,
            'mg': self.value * 100_000_000,
            'mkg': self.value * 100_000_000_000,
            'kg': self.value * 100,
            't': self.value / 10,
            'k': self.value * 500_000
        }

        return operations[self.item_change]


class Ton(WeightModel):

    def convert(self):
        operations = {
            'g': self.value * 1000_000,
            'mg': self.value * 1000_000_000,
            'mkg': self.value * 1000_000_000_000,
            'kg': self.value * 1000,
            'с': self.value * 10,
            'k': self.value * 5_000_000
        }

        return operations[self.item_change]


