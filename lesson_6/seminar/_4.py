# 4) Задание №4
# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.


def mystery(quest: str, answers: list, attempts: int):
    print(f"Загадка: {quest}")
    count = 0
    while count < attempts:
        answer = input("Введите ответ: ")
        if answer.lower() in map(str.lower, answers):
            return count + 1
        count += 1
    return 0


if __name__ == "__main__":
    question = "А и Б сидели на трубе, А упала Б пропала кто остался на трубе?"
    answers_ = ["и", "the i"]
    result = mystery(question, answers_, 3)
    print(f"Вы угадали с {result} попытки" if result != 0 else "Вы не угадали")
