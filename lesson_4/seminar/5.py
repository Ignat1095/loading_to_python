
def creat_dict():
    my_dict = {}
    start, end = map(int, input("Введите два числа через пробел: ").split())
    if start > end:
        start, end = end, start
    for i in range(start, end + 1):
        my_dict[chr(i)] = i
    return  my_dict
print(creat_dict())