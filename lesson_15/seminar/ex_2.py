"""
### Задание №2
📌На семинаре про декораторы был создан логирующий декоратор.
Он сохранял аргументы функции и результат её работы в файл.
📌Напишите аналогичный декоратор, но внутри используйте модуль logging.
"""
import logging
from functools import wraps

logging.basicConfig(filename="log.log",
                    encoding="utf-8",
                    level=logging.ERROR,
                    filemode="a")


def deco(func: callable):

    @wraps(func)
    def wrapper(*args, **kwargs):

        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Функция {func.__name__} с аргументами "
                          f"{args = }, {kwargs = } выдавала ошибку: {e = }")
            return None
    return wrapper


@deco
def div(a, b):
    return a/b

if __name__ == "__main__":
    div(2, 0)