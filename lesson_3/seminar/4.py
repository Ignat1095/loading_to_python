# ✔Создайте в ручную список, с повторяющимися элементами.
# ✔Удалите из него все элементы, которые встречаются дважды.

from random import randint


my_list = [randint(1, 20) for i in range(10)]
print(my_list)

new_list = [i for i in set(my_list) if my_list.count(i) == 2]
print(new_list)

