# 2) ✔Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

file = "D:/Учеба_GeekBrains/4 Python/loading_to_python/lesson_5/tusk_5.py"


def unpacking(data: str) -> (str, str, str):
    *way, name = data.split('/')
    name, extension = name.split('.')
    way = ''.join(way)
    return way, name, extension


unpack_file = unpacking(file)

print(f'   way    = {unpack_file[0]}')
print(f'  name    = {unpack_file[1]}')
print(f'extension = {unpack_file[2]}')
