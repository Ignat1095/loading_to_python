# ✔Функция получает на вход строку из двух чисел через пробел.
# ✔Сформируйте словарь, где ключом будет символ из Unicode, а значением — целое число.
# ✔Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.

def creat_dict():
    my_dict = {}
    start, end = map(int, input("Введите два числа через пробел: ").split())
    if start > end:
        start, end = end, start
    for i in range(start, end + 1):
        my_dict[chr(i)] = i
    return  my_dict
print(creat_dict())