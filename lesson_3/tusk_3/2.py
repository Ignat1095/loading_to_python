# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
from random import randint
import time


# print(my_list := [randint(1, 10) for i in range(10000)])
my_list = [randint(1, 10) for i in range(10000)]
print()


def one_line(data: list):
    return [item for item in set(data) if data.count(item) > 1]


def double_elements(data: list):
    new_list = []
    for i in data:
        if data.count(i) >= 2:
            if i not in new_list:
                new_list.append(i)

    return new_list


def copping_list(data) -> list:
    set_list = list(set(data))
    for i in range(len(set_list)):
        if set_list[i] in data:
            data.remove(set_list[i])
    new_list = list(set(data))
    return new_list


print('Вариант в одну строку')
start = time.time()  # точка отсчета времени
print(one_line(my_list))
end = time.time() - start  # собственно время работы программы
print(end)  # вывод времени


print('\nВариант медленный # 2')
start = time.time()  # точка отсчета времени
print(double_elements(my_list))
end = time.time() - start  # собственно время работы программы
print(end)  # вывод времени


print('\nВариант самый быстрый # 3')
start = time.time()  # точка отсчета времени
print(copping_list(my_list))
end = time.time() - start  # собственно время работы программы
print(end)  # вывод времени
