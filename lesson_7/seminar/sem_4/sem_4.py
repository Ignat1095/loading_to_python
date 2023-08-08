# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байтов, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байтов, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

from random import randint, choice


def give_name(min_size, max_size) -> str:
    bcd = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    aei = ['a', 'e', 'i', 'o', 'u', 'y']

    name = ''
    length = randint(min_size, max_size)
    for letter in range(length):
        consonant = choice(bcd)  # Согласная
        vowel = choice(aei)  # Гласная
        if letter % 2 != 0:
            name += "".join(vowel)
        else:
            name += "".join(consonant)
    return name


def crate_file(ext: str,
               min_name: int = 6, max_name: int = 30,
               min_size: int = 256, max_size: int = 4096,
               count_files: int = 42):

    for _ in range(count_files):
        with open(give_name(min_name, max_name) + ext, 'w', encoding='utf-8') as file:
            list_of_bytes = bytes([randint(0, 255) for i in range(min_size, max_size)])
            file.write(str(list_of_bytes))


def create_random_ext():
    ext = '.'.join(give_name(1, 5))
    crate_file(ext=ext)

if __name__ == "__main__":
    create_random_ext()
