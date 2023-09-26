"""
### Задание №4
📌Напишите для задачи 1 тесты pytest.
Проверьте следующие варианты:
📌возврат строки без изменений
📌возврат строки с преобразованием регистра без потери символов
📌возврат строки с удалением знаков пунктуации
📌возврат строки с удалением букв других алфавитов
📌возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""

from ex_1 import clean_text
import pytest


def test_clean_text_1():
    assert clean_text("give me a монеты"), "Тест 1 не пройден"


def test_clean_text_2():
    assert clean_text("Hello world 565!, Привет мир"), "Тест 2 не пройден"

if __name__ == "__main__":
    pytest.main()