# ✔Функция получает на вход список чисел.
# ✔Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# ✔Как вариант напишите сортировку пузырьком. Её описание есть в википедии.


my_list = [4, 8, 15, 16, 23, 42]

def sort_list(my_list):
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            if my_list[j] < my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]


sort_list(my_list)
print(sort_list(my_list))