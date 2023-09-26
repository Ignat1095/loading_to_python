"""
## Основы тестирования

### Задание №1
📌Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
📌Возвращается строка в нижнем регистре.

### Задание №2
📌Напишите для задачи 1 тесты doctest.
Проверьте следующие варианты:
📌возврат строки без изменений
📌возврат строки с преобразованием регистра без потери символов
📌возврат строки с удалением знаков пунктуации
📌возврат строки с удалением букв других алфавитов
📌возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""

from string import ascii_letters, punctuation


def clean_text(text: str) -> str:
    """
    Функция удаляет нелатинский текст.

        >>> clean_text("give me a монеты")
        'give me a '

        >>> clean_text("Hello world 565!, Привет мир")
        'hello world !,  '
    """
    return "".join(i for i in text
                   if i in ascii_letters + punctuation + " ").lower()

# print(clean_text("Hello world 565!, Привет мир"))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)