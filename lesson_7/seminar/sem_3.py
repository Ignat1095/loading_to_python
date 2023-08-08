# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
#
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю.
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.

def func(file_1, file_2, file_3):
    with (
        open(file_1, 'r', encoding="UTF-8") as file1,
        open(file_2, 'r', encoding="UTF-8") as file2,
        open(file_3, 'a', encoding="UTF-8") as file3
    ):
        numbers = file1.read().split('\n')
        names = file2.read().split('\n')

        if len(numbers) > len(names):
            names += names[:len(numbers)-len(names)]
        else:
            numbers += numbers[:len(names)-len(numbers)]

        for name, number in zip(names, numbers):
            if not name or not number:
                continue
            num_1, num_2 = map(float, number.split('|'))
            mult = num_1 * num_2
            if mult < 0:
                file3.write(f'{name.lower()} {abs(mult)}\n')
            else:
                file3.write(f'{name.upper()} {round(mult)}\n')


func("txt_1.txt", "txt_2.txt", "txt_3.txt")

