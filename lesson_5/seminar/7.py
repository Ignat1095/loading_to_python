# Задание №7
# ✔Создайте функцию-генератор.
# ✔Функция генерирует N простых чисел, начиная с числа 2.
# ✔Для проверки числа на простоту используйте правило: «число является простым,
# если делится нацело только на единицу и на себя».

def is_prime(digit):
    for i in range(2, digit):
        flag = False

        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                flag = True
                break
        if not flag:
            yield i


funk = is_prime(50)
for i in range(2, 20):
    print(next(funk, None))
