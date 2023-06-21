# ✔Функция получает на вход список чисел и два индекса.
# ✔Вернуть сумму чисел между переданными индексами.
# ✔Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.

text = 'У нас все хорошо!'

def sorted_unicod(text):
    my_list = []
    for i in text:
        if ord(i) not in my_list:
            my_list.append(ord(i))
    my_list.sort()
    return my_list

print(sorted_unicod(text))


