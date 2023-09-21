"""
### Задание №1
📌Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор,
пока он не введёт целое или вещественное число.
📌Обрабатывайте не числовые данные как исключения.
"""


def is_number():
    while True:
        try:
            number = float(input("Введите число: "))
            break
        except ValueError as e:
            print(f"Вы ввели не число: {e}")
    return number


print(is_number())

if __name__ == "__main__":
    print(is_number())