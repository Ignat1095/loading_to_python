# 2) Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

number, base = input('Введите число и систему, в которую хотите перевести через пробел: ').split()
number, base = int(number), int(base)


def number_converter(number:int, base: int) -> str:
    base_letters = "0123456789ABCDEF"
    num = number

    result = ''
    while number > 0:
        result = base_letters[number % base] + result
        number //= base

    print(f'Число {num} в {base} системе равно {result}')

number_converter(number, base)
