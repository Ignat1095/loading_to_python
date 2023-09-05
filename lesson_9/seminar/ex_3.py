# ### Задание №3
# 📌Напишите декоратор,
# который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает.
# При повторном вызове файл должен расширяться, а не перезаписываться.
# 📌Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# 📌Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# 📌Имя файла должно совпадать с именем декорируемой функции.
import json


def cash(func: callable):
    try:
        with open(func.__name__ + ".json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    def wrapper(*args, **kwargs):
        arg = str(args) + str(kwargs)
        result = func(*args, **kwargs)
        data.update({arg: result})
        with open(func.__name__ + ".json", "w") as file:
            json.dump(data, file, indent=4)
        return result
    return wrapper


@cash
def summa(one, two):
    return one * two

summa(10, 5)
summa(1012, 5)
