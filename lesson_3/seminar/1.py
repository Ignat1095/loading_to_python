# Задание №1
# ✔Вручную создайте список с целыми числами, которые повторяются.
# Получите новый список, который содержит уникальные (без повтора) элементы исходного списка.
# ✔*Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.

from random import randint

my_list = [randint(0, 20) for i in range(20)]

my_set_list = []
for i in my_list:
    if i not in my_set_list:
        my_set_list.append(i)
print(my_set_list)


set_list = list(set(my_list))
print('set = ', set_list)