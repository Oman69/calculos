import random
import string
from pydantic import BaseModel


class Password(BaseModel):
    count: int
    length: int
    ascii_low: bool
    ascii_upp: bool
    symbols: bool

    def create_pass(self):
        source = string.digits
        if self.ascii_low:
            source += string.ascii_lowercase
        if self.ascii_upp:
            source += string.ascii_uppercase
        if self.symbols:
            source += '~!@#$%^&*()_+'

        passwords = []
        for i in range(self.count):
            pass_str = ''
            for l in range(self.length):
                pass_str += random.choice(source)
            passwords.append(pass_str)
        return passwords


class RandomNumber(BaseModel):
    count: int
    start: int
    stop: int
    sorting: bool

    def create_numbers(self):
        numbers = []
        for i in range(self.count):
            num = random.randint(self.start, self.stop)
            numbers.append(num)
        if self.sorting:
            numbers.sort()
        return numbers


