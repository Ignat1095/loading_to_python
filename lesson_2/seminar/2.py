# Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок.
# Для каждого элемента в цикле выведите:
# ✔порядковый номер начиная с единицы
# ✔значение
# ✔адрес в памяти
# ✔размер в памяти
# ✔хэш объекта
# ✔результат проверки на целое число только если он положительный
# ✔результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните результаты.


data = [12, 12.12, 'abc', True, 12, 'abc']
count = 1
for i in data:
    types = ''
    if isinstance(i, int):
        # print("int ", end='')
        types = 'int'
    if isinstance(i, str):
        # print('str ', end='')
        types = 'str'
    print('№:', count, i,'type:', types, "id:", id(i), 'hash', hash(i))
    count += 1
