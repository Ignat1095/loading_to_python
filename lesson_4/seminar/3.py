# ✔Функция получает на вход строку из двух чисел через пробел.
# ✔Сформируйте словарь, где ключом будет символ из Unicode, а значением — целое число.
# ✔Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.

a, b = map(int, input("Два числа через пробел: ").split())


def unicode_integer(start, stop):
    unicode_int = {}
    start, stop = min(start, stop), max(start, stop)
    for i in range(start, stop + 1):
        unicode_int[chr(i)] = i
    return unicode_int


print(unicode_integer(a, b))
