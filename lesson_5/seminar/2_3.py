# Задание №2
# ✔Самостоятельно сохраните в переменной строку текста.
# ✔Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔Напишите преобразование в одну строку.
from pprint import pprint


dict_a = {i: ord(i) for i in 'Напишите преобразование в одну строку'}
pprint(dict_a, width=2)


# Задание №3
# ✔Продолжаем развивать задачу 2.
# ✔Возьмите словарь, который вы получили. Сохраните его итератор.
# ✔Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.
print()
iter_dict = iter(dict_a.items())
for i in range(20):
    print(next(iter_dict, None))
