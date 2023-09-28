"""
### Задание №4
📌Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
📌Преобразуйте его в дату в текущем году.
📌Логируйте ошибки, если текст не соответствует формату.

### Задание №5
📌Дорабатываем задачу 4.
📌Добавьте возможность запуска из командной строки.
📌При этом значение любого параметра можно опустить.
В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
📌*Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые, т.е не мая, а 5.
"""
from datetime import datetime, date, timedelta
import logging
from functools import wraps
import argparse

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


MONTHS = ("   ", "янв", "фев", "мар", "апр", "мая", "июн", "июл", "авг", "сен", "окт", "ноя", "дек")
WEEKDAYS = ("пон", "вто", "сре", "чет", "пят", "суб", "вос")


@deco
def create_date(data: str):
    date_ = date.today().year
    day_, weekday_, month_ = data.split()

    day_ = int(day_[0])
    weekday_ = WEEKDAYS.index(weekday_[:3])
    month_ = MONTHS.index(month_[:3])

    start_data = date(year=date_, month=month_, day=day_)
    count = 0
    for _ in range(32):
        if start_data.weekday() == weekday_:
            count += 1
            if count == day_:
                return start_data
        # print(start_data, start_data.weekday())
        start_data += timedelta(days=1)

    raise ValueError


def pars():
    parser = argparse.ArgumentParser(description='My first argument parser')
    parser.add_argument('-d', '--day', type=str)
    parser.add_argument('-w', '--weekday', type=str)
    parser.add_argument('-m', '--month', type=str)
    args = parser.parse_args()
    return create_date(f'{args.day} {args.weekday} {args.month}')

if __name__ == "__main__":
    # text = "1-й четверг ноября"
    # text2 = "3-я среда мая"
    # print(create_date(text))
    # print(create_date(text2))
    print(pars())