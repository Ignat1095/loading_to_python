# ✔Пользователь вводит строку текста.
# ✔Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# ✔Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
# ✔Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.

my_text = "Пользователь вводит строку текста.".lower()
text = my_text.replace(" ", "")
print(text)

my_dict1 = {}
print()
for i in sorted(set(text)):
    my_dict1[i] = text.count(i)
print('my_dict.count = ', my_dict1)


my_dict2 = {}
for i in sorted(text):
    my_dict2[i] = my_dict2.get(i, 0) + 1
print('my_dict.get   = ', my_dict2)
