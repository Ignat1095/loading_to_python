"""
### Задание №3
📌Доработаем задачу 2.
📌Сохраняйте в лог файл раздельно:
* уровень логирования,
* дату события,
* имя функции (не декоратора),
* аргументы вызова,
* результат.
"""

import logging
from functools import wraps

FORMAT = '{levelname:<8} - {asctime}.В модуле "{name}"' \
         'в строке {lineno:03d} функция "{funcName}()"' \
         'в {created} секунд записала сообщение:{msg}'

logging.basicConfig(filename="log.log",
                    format=FORMAT,
                    style="{",
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
    return a / b


if __name__ == "__main__":
    div(2, 0)
