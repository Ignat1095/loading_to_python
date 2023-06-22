# ✔Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔Строки нумеруются начиная с единицы.
# ✔Слова выводятся отсортированными согласно кодировке Unicode.
# ✔Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.


text = "Арбуз Напишите функцию, которая принимает строку текста."


def sort_text(text: str):
    text_list = text.lower().replace(',', '').replace('.', '').split()
    text_list.sort(key=len, reverse=True)
    max_len = len(max(text_list, key=len))
    for i, el in enumerate(text_list, 1):
        print(f'{i:>2}. {el:.>{max_len}}')

sort_text(text)



