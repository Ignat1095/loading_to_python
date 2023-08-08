# 2) Задание №2
# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# # Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

from random import randint as rd


def what_number(min_=1, max_=20, tries=5):
    if min_ > max_:
        min_, max_ = max_, min_
    number = rd(min_, max_)
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


if __name__ == "main":
    print(what_number(1, 20, 5))
