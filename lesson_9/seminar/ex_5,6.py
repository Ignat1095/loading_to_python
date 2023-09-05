# ### Задание №5
# 📌Объедините функции из прошлых задач.
# 📌Функцию угадайку задекорируйте:
# * декораторами для сохранения параметров,
# * декоратором контроля значений,
# * декоратором для многократного запуска.
# 📌Выберите верный порядок декораторов.


### Задание №6
# 📌Доработайте прошлую задачу добавив декоратор wraps в каждый из декораторов.

import json
from functools import wraps


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


def param(count: int = 3):
    def decor(func):
        my_list = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(count):
                result = func(*args, **kwargs)
                my_list.append(result)
            return my_list
        return wrapper
    return decor


@cash
@param(3)
def summa(one, two):
    return one * two

print(summa(10, 5))

