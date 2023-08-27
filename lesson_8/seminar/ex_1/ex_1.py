# ### Задание №1
# 📌Вспоминаем задачу 3 из прошлого семинара.
# Мы сформировали текстовый файл с псевдоименами и произведением чисел.
# 📌Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# 📌Имена пишите с большой буквы.
# 📌Каждую пару сохраняйте с новой строки.
import json


def txt_to_json(old_data: str,
                new_data: str):

    with open(old_data, 'r', encoding="utf-8") as old_file:
        data = old_file.read()[:-1].split('\n')
        data = [{i.split()[0].capitalize(): float(i.split()[1])} for i in data]

    with open(new_data, "w", encoding="utf-8") as new_file:
        json.dump(data, new_file, indent=4)


if __name__ == "__main__":
    txt_to_json("ex_1_txt.txt", "new_file.json")
