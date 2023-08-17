from random import randint, choice
from os import getcwd, listdir, mkdir

__all__ = ['give_name', 'create_file']


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


def create_file(ext: str, directory: str = None,
                min_name: int = 5, max_name: int = 10,
                min_size: int = 256, max_size: int = 4096,
                count_files: int = 42):
    if not directory:
        directory = getcwd() + '\\'
    else:
        if directory not in listdir():
            mkdir(directory)
        directory = getcwd() + '\\' + directory + '\\'

    for _ in range(count_files):
        with open(directory + give_name(min_name, max_name) + ext, 'w', encoding='utf-8') as file:
            list_of_bytes = bytes([randint(0, 255) for i in range(min_size,
                                                                  max_size)])
            file.write(str(list_of_bytes))


if __name__ == "__main__":
    extension = ('.txt', '.doc', '.pdf', '.json', '.csv')
    create_file(ext=choice(extension), directory="test_dir", count_files=3)
