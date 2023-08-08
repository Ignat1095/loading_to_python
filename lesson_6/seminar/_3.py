# 3) Задание №3
# Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

from random import randint as rd
import sys


def what_number(_min=1, _max=20, tries=5):
    if _min > _max:
        _min, _max = _max, _min
    number = rd(_min, _max)
    count = 1
    while count <= tries:
        print(f"Попытка № {count}")
        try:
            tmp = int(input("Введите число: "))
        except:
            print("Нужно ввести ЦЕЛОЕ число!")
        if tmp < number:
            print("Больше! ")
        elif tmp > number:
            print("Меньше! ")
        else:
            return True
        count += 1
    return False


if __name__ == "__main__":
    if len(sys.argv) == 2:
        tries = int(sys.argv[1])
        print(what_number(tries=tries))
    elif len(sys.argv) == 4:
        min_, max_, tries = (int(i) for i in sys.argv[1:])
        print(what_number(min_, max_, tries))
    else:
        print("Неверное кол-во аргументов. ")
