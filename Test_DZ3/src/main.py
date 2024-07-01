class Calculator:

    def add(self, value_left, value_right) -> float:
        if not(isinstance(value_right, (int, float))) and not(isinstance(value_left, (int, float))):
            raise TypeError

        return value_left + value_right

    def subtract(self, value_left, value_right) -> float:
        if not (isinstance(value_right, (int, float))) and not (isinstance(value_left, (int, float))):
            raise TypeError

        return value_left - value_right

    def multiply(self, value_left, value_right) -> float:
        if not (isinstance(value_right, (int, float))) and not (isinstance(value_left, (int, float))):
            raise TypeError

        return value_left * value_right

    def divide(self, value_left, value_right) -> float:
        if not (isinstance(value_right, (int, float))) and not (isinstance(value_left, (int, float))):
            raise TypeError

        try:
            return value_left / value_right

        except ZeroDivisionError:
            raise ZeroDivisionError



class Array:

    def __init__(self, args):
        self.array = args

    def sum(self) -> float:

        if not(isinstance(self.array, list)) :
            raise TypeError

        summa = 0

        for i in self.array:
            if not(isinstance(i, (int, float))):
                raise TypeError
            summa += i

        return summa

    def multiplys(self) -> float:
        if not(isinstance(self.array, list)) :
            raise TypeError

        if not(self.array):
            return 0

        multiply = 1

        for i in self.array:
            if not(isinstance(i, (int, float))):
                raise TypeError

            multiply *= i

        return multiply

    def averages(self) -> float:
        if not(isinstance(self.array, list)) :
            raise TypeError

        for i in self.array:
            if not(isinstance(i, (int, float))):
                raise TypeError
        try:
            return self.sum() / len(self.array)

        except ZeroDivisionError:
            raise ZeroDivisionError


class User:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        User.count += 1

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def up_age(self):
        try:
            self.age += 1
            return self.age

        except TypeError:
            raise TypeError

