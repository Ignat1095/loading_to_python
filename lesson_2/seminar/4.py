# Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
# ✔Диаметр не превышает 1000 у.е.
# ✔Точность вычислений должна составлять не менее 42 знаков после запятой.
from math import pi
from decimal import Decimal, getcontext

getcontext().prec = 100  # Округление до 42


def circle(diameter):
    square = Decimal(diameter ** 2 / 4) * Decimal(pi)
    circumference = Decimal(pi) * Decimal(diameter)
    print(f'Площадь = {square}\nДлинна окр. = {circumference}')
    print(len(str(square)), len(str(circumference)))


print(len(str(pi)))
diameter = int(input("Введите диаметр: "))
circle(diameter)
