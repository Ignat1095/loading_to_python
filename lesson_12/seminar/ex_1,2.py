""" ### Задание №1  
📌Создайте класс-функцию, который считает факториал числа при вызове экземпляра.  
📌Экземпляр должен запоминать последние k значений.  
📌Параметр k передаётся при создании экземпляра.  
📌Добавьте метод для просмотра ранее вызываемых значений и их факториалов.

### Задание №2
📌Доработаем задачу 1.
📌Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.
"""
import json


class MyFac:
    def __init__(self, size: int):
        self._size = size
        self.__data = []

    def history(self):
        return self.__data

    def __call__(self, number: int):
        result = 1
        for i in range(1, number + 1):
            result *= i

        if len(self.__data) >= self._size:
            self.__data.pop(0)
        self.__data.append({f'{number}!': result})
        return result

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open("ex_2.json", "w") as j_file:
            json.dump(self.__data, j_file, indent=4)

if __name__ == "__main__":
    f1 = MyFac(size=5)
    with f1:
        for num in range(1, 10):
            print(f1(num))

    print(f1.history())