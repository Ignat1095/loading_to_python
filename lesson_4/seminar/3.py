# ✔Функция получает на вход строку из двух чисел через пробел.
# ✔Сформируйте словарь, где ключом будет символ из Unicode, а значением — целое число.
# ✔Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.

a, b = map(int, input("Два числа через пробел: ").split())


def unicode_integer(start, stop):
    unicode_int = {}
    a, b = min(start, stop), max(start, stop)
    for i in range(a, b + 1):
        unicode_int[chr(i)] = i
    print(unicode_int, sep='\n')


print(unicode_integer(a, b))




def creat_dict():
    my_dict = {}
    start, end = map(int, input("Введите два числа через пробел: ").split())
    if start > end:
        start, end = end, start
    for i in range(start, end + 1):
        my_dict[chr(i)] = i
    return  my_dict
# print(creat_dict())