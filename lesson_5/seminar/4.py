# Задание №4
# ✔Создайте генератор чётных чисел от нуля до 100.
# ✔Из последовательности исключите числа, сумма цифр которых равна 8.
# ✔Решение в одну строку.

my_test = (i for i in range(2, 101, 2) if sum(map(int, str(i))) != 8)
for i in range(50):
    print(next(my_test, None))
