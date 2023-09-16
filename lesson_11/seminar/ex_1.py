"""
Задание №1
📌Создайте класс Моя Строка, где:
📌будут доступны все возможности str
📌дополнительно хранятся имя автора строки и время создания (time.time)
"""
import time


class MyStr(str):
    """
    documentation
    """
    def __new__(cls, value: str, name: str):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.time_create = time.time()
        instance.value = value
        return instance

    def __repr__(self):
        return f"{self.value = }, name = {self.name = } {round(self.time_create)}"


a = MyStr("my str", name="Ivan")

print(a)
print(repr(a))
print(MyStr.__doc__)