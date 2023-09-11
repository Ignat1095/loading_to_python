# ### Задание №2
# 📌Создайте класс прямоугольник.
# 📌Класс должен принимать длину и ширину при создании экземпляра.
# 📌У класса должно быть два метода, возвращающие
# периметр и площадь.
# 📌Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

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


if __name__ == "__main__":
    first = Rectangle(2, 4)
    print(f'{first.perimetr() = }, {first.square() = }')

    print("---")
    
    second = Rectangle(2)
    print(f'{second.perimetr() = }, {second.square() = }')