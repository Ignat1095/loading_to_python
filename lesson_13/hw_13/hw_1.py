"""
Задание:
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
Напишите к ним классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода.
Например, нельзя создавать прямоугольник со сторонами отрицательной длины.
"""


class ExceptionPositive(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value = }, должно быть больше 0 "


class Rectangle:

    def __init__(self, length: int, width: int = None):
        if length <= 0:
            raise ExceptionPositive(length)
        self.length = length
        if width <= 0:
            raise ExceptionPositive(width)
        if width:
            self.width = width
        else:
            self.width = length

    def perimetr(self):
        return (self.length + self.width) * 2

    def square(self):
        return self.length * self.width

    def __add__(self, other):
        return Rectangle(length=self.length + other.length,
                         width=self.width + other.width)

    def __sub__(self, other):
        return Rectangle(length=self.length - other.length,
                         width=self.width - other.width)

    def __eq__(self, other: "Rectangle"):
        return self.square() == other.square()

    def __le_(self, other: "Rectangle"):
        return self.square() <= other.square()

    def __lt_(self, other: "Rectangle"):
        return self.square() < other.square()

    def __ge_(self, other: "Rectangle"):
        return self.square() >= other.square()

    def __gt__(self, other: "Rectangle"):
        return self.square() > other.square()

r1 = Rectangle(2, -4)
print(r1.square())