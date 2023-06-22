# ✔Функция получает на вход словарь с названием компании в качестве ключа и
# списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔Вычислите итоговую прибыль или убыток каждой компании.
# Если все компании прибыльные, верните истину, а если хотя бы одна убыточная — ложь.


def profit(my_dict: dict[str:[list]]) -> bool:
    # # for value in my_dict.values():
    # #     if sum(value) < 0:
    # #         return False
    # #     else:
    # #         return True
    if all(map(lambda x: sum(x) > 0, my_dict.values())):
        return True
    else:
        return False


my_dict = {"Asus": [100, -200],
           "Apple": [100, 200],
           "Samsung": [200, 200]}


print(profit(my_dict))
# a = [100, -200]
# print(sum(a))
