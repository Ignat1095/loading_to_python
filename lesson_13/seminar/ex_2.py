"""
### Задание №2
📌Создайте функцию аналог get для словаря.
📌Помимо самого словаря функция принимает ключ и значение по умолчанию.
📌При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
📌Реализуйте работу через обработку исключений.
"""


class GetDict(dict):
    def get_dict(self, key_, value=None):
        try:
            return self[key_]
        except KeyError as e:
            print(f"Ошибка {e}")

mg = GetDict({"papa": "father"})
print(mg)
print(mg.get("papa"))

mg.update({"wfreg": "123"})
print(mg["qer"])
