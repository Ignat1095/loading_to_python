# Напишите функцию группового переименования файлов.

# Она должна:

# Принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# Принимать параметр количество цифр в порядковом номере.
# Принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# Принимать параметр расширение конечного файла.

# Принимать диапазон сохраняемого оригинального имени.
# Например, для диапазона[3, 6] берутся буквы с 3 по 6 из исходного имени файла.

# К ним прибавляется желаемое конечное имя, если оно передано.

# Далее счётчик файлов и расширение.

from os import chdir, getcwd
from pathlib import Path


def refactor_file(directory: str | Path = "test_dir"):
    chdir(directory)
    count = 1
    for file in Path(getcwd()).iterdir():
        if file.is_dir():
            continue

        *way, name = str(file).split("\\")
        way = "\\".join(way)
        new_name = rename(name, count)
        count += 1
        file.replace(f"{way}\\{new_name}")


def rename(name: str, count: int = 1):
    """
    Переименование имени если кончается на гласную,
    Добавление порядкового номера
    :param name:
    :param count:
    :return:
    """
    name, ext = name.split(".")
    name, *old_number = name.split("_")
    ext = "." + ext

    if name[-1] in ['a', 'e', 'i', 'o', 'u', 'y']:
        new_name = name[0:3] + "_" + str(count) + ext
    else:
        new_name = name + "_" + str(count) + ext
    return new_name


refactor_file()
