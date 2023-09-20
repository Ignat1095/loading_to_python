"""
### Задание №4
📌Доработайте класс прямоугольник из прошлых семинаров.
📌Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений (отрицательных).
📌Используйте декораторы свойств.

### Задание №5
📌Доработаем прямоугольник и добавим экономию памяти
для хранения свойств экземпляра без словаря __dict__.

### Задание №6
📌Изменяем класс прямоугольника.
📌Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.
"""


class Side:
    def __set_name__(self, owner, name):
        self._param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self._param_name)

    def __Set__(self, instance, value):
        self.validate(value)
        setattr(instance, self._param_name, value)

    @staticmethod
    def validate(value):
        if value <= 0:
            raise ValueError("Значение должно быть больше 0")


class Rectangle:
    # __slots__ = ("__length", "__width")

    __width = Side()
    __length = Side()

    def __init__(self, length: int, width: int = None):
        self.__length = length
        if width:
            self.__width = width
        else:
            self.__width = length

    def perimetr(self):
        return (self.__length + self.__width) * 2

    def square(self):
        return self.__length * self.__width


if __name__ == "__main__":
    f1 = Rectangle(length=-4, width=-6)
    # f1._Rectangle__length = -2
    f1.width = 4
    f1.width = 4
    print(f1.square())

