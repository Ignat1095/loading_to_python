# 4. Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.

from random import randint

number = randint(0, 1000)
# print(number)
print("Попробуйте угадать число: ")


def think_of_number(count):
    subsequently = 10
    answer = int(input(f"\nПопытка № {count}: "))

    if count < subsequently:
        if answer > number:
            print("\nМеньше!")
            return think_of_number(count + 1)
        elif answer < number:
            print("\nБольше!")
            return think_of_number(count + 1)
        elif answer == number:
            print("\nВы угадали!")
    else:
        print("Вы не угадали...")

count = 1
think_of_number(count)
