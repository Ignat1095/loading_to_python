# Пользователь вводит строку текста.
# Вывести каждое слово с новой строки.
# ✔Строки нумеруются начиная с единицы.
# ✔Слова выводятся отсортированными согласно кодировке Unicode.
# ✔Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

text = 'Всем привет. Шла Саша по шоссе.'.lower().replace(".", "").split()
print(text)
text.sort()
print(text)

len_max = len(max(text, key=len))


for i, el in enumerate(text, 1):
    print(f'{i} {el:.>{len_max}}')
