# ### Задание №1
# 📌Создайте функцию-замыкание, которая запрашивает два целых числа:
# * от 1 до 100 для загадывания,
# * от 1 до 10 для количества попыток
# 📌Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.
#
# ### Задание №2
# 📌Дорабатываем задачу 1.
# 📌Превратите внешнюю функцию в декоратор.
# 📌Он должен проверять входят ли переданные в функцию - угадайку. Числа в диапазоны [1, 100]и[1, 10].
# 📌Если не входят, вызывать функцию со случайными числами из диапазонов.
from random import randint


def game(number: int, tries: int):
    def guessing_game():
        for _ in range(tries):
            if number == int(input("Введите число: ")):
                return True
        return False
    return guessing_game


def gaming(func):
    def wrapper(number: int, tries: int):
        if not 100 >= number >= 1:
            number = randint(1, 101)
        if not 10 >= tries >= 1:
            tries = randint(1, 11)
        return func(number, tries)
    return wrapper


@gaming
def guess_num(number: int, tries: int):
    print(number, tries)
    for _ in range(tries):
        if number == int(input("Введите число: ")):
            return True
    return False


if __name__ == "__main__":
    # my_game_1 = game(10, 3)()
    # print(f"{my_game_1 = }")

    my_game_2 = guess_num(102, 11)
    print(f"{my_game_2 = }")
