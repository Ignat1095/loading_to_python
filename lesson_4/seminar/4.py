# ✔Функция получает на вход список чисел.
# ✔Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# ✔Как вариант напишите сортировку пузырьком. Её описание есть в википедии.
from random import randint

my_list = [randint(1, 10) for i in range(10)]
print(my_list)
for j in range(len(my_list)-1):
    for i in range(len(my_list)-1-j):
        if my_list[i] > my_list[i+1]:
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
print(my_list)
