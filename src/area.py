from math import pi, sqrt
from abc import ABC, abstractmethod
from typing import Optional


class Figure(ABC):
    @abstractmethod
    def get_area(self) -> float:
        raise NotImplementedError

    @classmethod
    def get_abstract_area(cls, *sides: float) -> Optional[float]:
        for subclass in cls.__subclasses__():
            try:
                if len(sides) == len(subclass(*sides).__dict__):
                    result = subclass(*sides).get_area()
                    return result

            except TypeError:
                continue

        raise TypeError('A figure with this number of sides is not defined')


class Circle(Figure):
    def __init__(self, radius: float) -> None:
        self.radius = radius
        if not isinstance(self.radius, (float, int)):
            raise ValueError('Unexpected type of values')
        if self.radius <= 0:
            raise ValueError('There is no circle with the specified radius')

    def get_area(self) -> float:
        area = pi * self.radius ** 2
        return area


class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float) -> None:
        sides = a, b, c

        if not all(isinstance(value, (float, int)) for value in sides):
            raise ValueError('Unexpected type of values')

        max_side = max(sides)
        if max_side >= sides[sides.index(max_side) - 2] + sides[sides.index(max_side) - 1] or \
                not all(value > 0 for value in sides):
            raise ValueError('There is no triangle with the specified sides')
        self.a, self.b, self.c = sides

    def get_area(self) -> float:
        half_meter = sum((self.a, self.b, self.c)) / 2
        area = sqrt(half_meter * (half_meter - self.a) * (half_meter - self.b) * (half_meter - self.c))
        return area

    def is_right(self) -> str:
        sides = (self.a, self.b, self.c)
        max_side = max(sides)
        if max_side ** 2 == sides[sides.index(max_side) - 1] ** 2 + sides[sides.index(max_side) - 2] ** 2:
            return 'Треугольник правильный'

        else:
            return 'Треугольник неправильный'
