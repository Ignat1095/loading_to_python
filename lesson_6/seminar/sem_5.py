# 5) Задание №5
# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

from _4 import mystery

_result = dict()


def get_mystery_dict(riddles: dict):
    global _result
    for question, answers in riddles.items():
        _result[question] = mystery(question, answers, 3)
        print()
    return _result


def show_result():
    global _result
    for question, _result in _result.items():
        print(f"С загадкой: {question}")
        print(f"Ваш результат:", end="")
        print(f"Вы угадали с {_result} попытки\n" if _result != 0 else "Вы не угадали\n")


if __name__ == "__main__":
    riddles_ = {
        "А и Б сидели на трубе, А упала Б пропала кто остался на трубе?": ["и", "i"],
        "Без чего ничего никогда не бывает?": ["Название", "name"]
    }
    get_mystery_dict(riddles_)
    show_result()

