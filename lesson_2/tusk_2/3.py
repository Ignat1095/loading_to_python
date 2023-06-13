# 3) Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму = и произведение * дробей.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

fractal_1 = input("Введите первую дробь: ")
fractal_2 = input("Введите вторую дробь: ")


def convert_fractal(fractal: str) -> tuple[int:int]:
    """
    Конвертируем дробь в кортеж
    """
    numerator, denominator = fractal.split('/')
    return int(numerator), int(denominator)


def reduction(numerator: int, denominator: int) -> tuple[str, str]:
    """
    Сокращение на максимальное число обеих дробей
    """

    def all_devs(number: int) -> set[int]:
        all_dev = set()
        for dev in range(1, number // 1 + 1):  # почему 1+1?
            if not number % dev:
                all_dev.add(dev)
        return all_dev

    numerator_dev = all_devs(numerator)
    denominator_dev = all_devs(denominator)
    reduct = max(numerator_dev.intersection(denominator_dev))
    return str(numerator // reduct), str(denominator // reduct)


def summ(first: str, second: str) -> str:
    a, b, = convert_fractal(first), convert_fractal(second)
    numerator = a[0] + b[0]
    denominator = a[1]
    if a[1] != b[1]:
        numerator = a[0] * b[1] + a[1] * b[0]
        denominator = a[1] * b[1]
    return '/'.join(reduction(numerator, denominator))


def multi(first: str, second: str) -> str:
    a, b = convert_fractal(first), convert_fractal(second)
    numerator = a[0] * b[0]
    denominator = a[1] * b[1]
    return '/'.join(reduction(numerator, denominator))


print('Сумма: ',summ(fractal_1, fractal_2))
print('Произведение', multi(fractal_1, fractal_2))
print()
# Проверка:
print('Сумма: ', Fraction(*convert_fractal(fractal_1)) + Fraction(*convert_fractal(fractal_2)))
print('Произведение', Fraction(*convert_fractal(fractal_1)) * Fraction(*convert_fractal(fractal_2)))
