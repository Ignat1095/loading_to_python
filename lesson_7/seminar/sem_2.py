# Задание №2
# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв,
# среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

import random


def fill_file(file, count_lines):
    bcd = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    aei = ['a', 'e', 'i', 'o', 'u', 'y']

    with open(file, 'a', encoding='UTF-8') as file:
        for i in range(count_lines):
            length = random.randint(4, 7)
            name = ""
            for letter in range(length):
                consonant = random.choice(bcd)  # Согласная
                vowel = random.choice(aei)  # Гласная
                if letter % 2 != 0:
                    name += "".join(vowel)
                else:
                    name += "".join(consonant)
            print(f'{name.capitalize()}', file=file)


fill_file('txt_2.txt', 3)
