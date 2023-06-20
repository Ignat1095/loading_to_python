# ✔Создайте в ручную список, с повторяющимися элементами.
# ✔Удалите из него все элементы, которые встречаются дважды.

from random import randint
from itertools import groupby

my_list = [randint(1, 10) for i in range(1, 20)]

print(my_list)

# № 1
temp = []
for i in my_list:
    if i not in temp:
        temp.append(i)
new_1_list = temp
print('new_1_list = ', new_1_list)


# № 2
new_2_list = list(set(my_list))
print('new_2_list = ', new_2_list)




# № 3
my_list.sort()
new_3_list = [i for i, _ in groupby(my_list)]

print('new_3_list = ', new_3_list)