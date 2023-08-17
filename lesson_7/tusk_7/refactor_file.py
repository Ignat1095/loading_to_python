# Напишите функцию группового переименования файлов.

# Она должна:

# Принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# Принимать параметр количество цифр в порядковом номере.
# Принимать параметр расширение исходного файла.  Переименование должно работать только для этих файлов внутри каталога.
# Принимать параметр расширение конечного файла.

# Принимать диапазон сохраняемого оригинального имени.
# Например, для диапазона[3, 6] берутся буквы с 3 по 6 из исходного имени файла.

# К ним прибавляется желаемое конечное имя, если оно передано.
# Далее счётчик файлов и расширение.
#
# Пример:
# rename(wanted_name = "video", count_nums=3, extension_old=".txt", extension_new=".csv", diapazon=[3, 6])
# foto_2002.txt -> o_20video001.csv

from os import chdir, getcwd, listdir, mkdir
from pathlib import Path


def refactor_file(new_name: str,
                  old_ext: str, new_ext: str = None,
                  count_digits: int = 3,
                  range_name: range = (3, 6),
                  directory: str | Path = "test_dir"):
    if directory not in listdir():
        mkdir(directory)
    directory = getcwd() + '\\' + directory + '\\'
    chdir(directory)
    count = 1
    if new_ext is None:
        new_ext = old_ext
    for file in Path(getcwd()).iterdir():
        if file.is_file() and file.suffix == old_ext:
            new_file_name = f"{file.stem[range_name[0]:range_name[1]]}{new_name}_{count:0{count_digits}}{new_ext}"
            count += 1
            file.replace(new_file_name)
    if count > 1:
        print(f"Переименовано {count} файл(ов) {{old_ext}} в {{new_ext}}")
    else:
        print(f"Файлов с расширением {{old_ext}} не существует!")


refactor_file("_видео", old_ext=".txt", new_ext=".jpg")
