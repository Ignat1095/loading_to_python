# ### Задание №5
# 📌Дорабатываем класс прямоугольник из прошлого семинара.
# 📌Добавьте возможность:
#   сложения и вычитания.
# 📌При этом должен создаваться новый экземпляр прямоугольника.
# 📌Складываем и вычитаем периметры, а не длину и ширину.
# 📌При вычитании не допускайте отрицательных значений.

class Rectangle:

    def __init__(self, length: int, width: int = None):
        self.length = length
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


first = Rectangle(4, 6)
print(f'{first.perimetr() = }, {first.square() = }')

print("---")

second = Rectangle(2)
print(f'{second.perimetr() = }, {second.square() = }')

third = first - second
print(f'{third.perimetr() = }, {third.square() = }')

print(third < first)
print(third >= first)