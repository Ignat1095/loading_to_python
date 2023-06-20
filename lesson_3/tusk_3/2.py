# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
from random import randint

print('Ваш вариант')

print(my_list := [randint(1, 15) for i in range(10)])
print([item for item in set(my_list) if my_list.count(item) > 1])

print('\nМой вариант')

# my_list = [randint(1, 15) for i in range(10)]
print(my_list)


def copping_list() -> list:
    set_list = list(set(my_list))
    for i in range(len(set_list)):
        if set_list[i] in my_list:
            my_list.remove(set_list[i])
    new_list = list(set(my_list))
    return new_list


print(copping_list())
