# ✔Создайте в ручную список, с повторяющимися целыми числами.
# ✔Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# ✔Нумерация начинается с единицы.
from random import randint

my_list = [randint(1, 10) for i in range(10)]
print(my_list)

new_list = []

for i, el in enumerate(my_list, 1):
    if el % 2 == 1:
        new_list.append(i)
print(new_list)
