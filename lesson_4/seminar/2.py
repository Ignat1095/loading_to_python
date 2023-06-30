# ✔Напишите функцию, которая принимает строку текста.
# ✔Сформируйте список с уникальными кодами
# Unicode каждого символа введённой строки отсортированный по убыванию.

text = 'Напишите функцию,./    00'


def unicode_sort(text):
    text_sort = []
    for i in text:
        text_sort.append(ord(i))

    return sorted(text_sort)

print(unicode_sort(text))