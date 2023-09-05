# ### Задание №4
# 📌Создайте декоратор с параметром.
# 📌Параметр - целое число, количество запусков декорируемой функции.

def param(count: int = 3):
    def decor(func):
        my_list = []

        def wrapper(*args, **kwargs):
            for i in range(count):
                result = func(*args, **kwargs)
                my_list.append(result)
            return my_list
        return wrapper
    return decor


@param(5)
def mult(one, two):
    return one * two


print(mult(4, 6))
