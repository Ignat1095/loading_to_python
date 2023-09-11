# ### Задание №1
# 📌Создайте класс окружность.
# 📌Класс должен принимать радиус окружности при создании экземпляра.
# 📌У класса должно быть два метода,
# возвращающие длину окружности
# и её площадь.

import math


class Circle:
    _pi = math.pi

    def __init__(self, radius):
        self.radius = radius

    def perimetr(self):
        return self._pi * self.radius * 2

    def square(self):
        return self._pi * self.radius ** 2


first = Circle(10)
