# Функция получает на вход список чисел и два индекса.
# Вернуть сумму чисел между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.

def sum_of_number(numbers, start, end):
    if start < 0:
        start = 0

    if start > len(numbers):
        return None

    return sum(numbers[start:end])

a = [1, 123, 3567, 8756, 34, 23, 65, 23, 63, 23]

print(sum_of_number(a, 1, 5))
