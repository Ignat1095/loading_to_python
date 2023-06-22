# Задание №3
# ✔Создайте вручную кортеж содержащий элементы разных типов.
# ✔Получите из него словарь списков, где: ключ — тип элемента, значение — список элементов данного типа.

my_tuple = (123, 123.456, 'master', True, 123, False, [1, 2], [2, 3])

my_dict = {}

for i in my_tuple:
    if type(i) not in my_dict:
        my_dict[type(i)] = [i]
    else:
        my_dict[type(i)].append(i)

print(my_dict)
