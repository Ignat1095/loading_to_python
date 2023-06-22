# ✔Функция получает на вход список чисел и два индекса.
# ✔Вернуть сумму чисел между переданными индексами.
# ✔Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.
from random import randint


my_list = [randint(1, 10) for i in range(10)]
print(my_list)
a, b = map(int, input("Два числа через пробел: ").split())
if a > b:
    a, b = b, a
if a < 0:
    a = 0
if b > len(my_list):
    b = len(my_list)
result = sum(my_list[a:b+1])
print(result)


