"""
### Задание №1
📌Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
📌Например отлавливаем ошибку деления на ноль.
"""
import logging

logging.basicConfig(filename="log.log",
                    encoding="utf-8",
                    level=logging.ERROR)

# logging.error("На ноль нельзя")


def div(a, b):
    try:
        # res = a/b
        return a/b
    except ZeroDivisionError:
        logging.error(f"b = {b}")
        return None


if __name__ == "__main__":
    div(2, 0)

# logger = logging.getLogger(__name__)
# logging.basicConfig(format=FORMAT, style="{", level=logging.INFO)

# logger.debug("Очень подробная инфо")
# logger.info("")
# logger.warning("")
# logger.error("")
# logger.critical("")
