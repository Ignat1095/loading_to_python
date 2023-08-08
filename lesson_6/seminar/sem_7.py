# 7) Задание №7
# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает:
# истину, если дата может существовать или
# ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне[1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

from datetime import datetime as dt

__all__ = ["check_date"]


def check_date(current_date):
    try:
        day, month, year = map(int, current_date.split("."))
    except:
        return False
    try:
        dt(year=year, month=month, day=day)
    except:
        return False
    return True


print(check_date("10.02.1995"))
print(check_date("10.14.1995"))


if __name__ == "__main__":
    __all__ = ["check_date"]


