# ### Задача 3.
# Возьмите 1-3 любые задания из прошлых семинаров, (например, сериализация данных) которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства.
# Задания должны решаться через вызов методов экземпляра.
import csv
import json


class ImportTo:
    # _tmp_data = {}

    def __init__(self, data):
        self.data = data

    def create_json(self, file_name):
        with open(f"{file_name}.json", "w", encoding="utf-8") as f_json:
            json.dump(self.data, f_json, indent=4, ensure_ascii=False)

    def create_csv(self, file_name):
        with open(f"{file_name}.csv", "w", encoding="utf-8", newline="") as f_csv:
            csv_writer = csv.writer(f_csv)
            csv_writer.writerows(self.data)

    def create_txt(self, file_name):
        with open(f"{file_name}.txt", "w", encoding="utf-8") as t_file:
            for line in self.data:
                print(" ".join(line))
                t_file.write(" ".join(line)+"\n")


with open("phonebook.txt", "r", encoding="utf-8") as file:
    phonebook = []
    for item in file:
        phone, *description = item.split()
        phonebook.append([phone, " ".join(description)])

file = ImportTo(phonebook)
file.create_json("new_file")
file.create_csv("new_file")
file.create_txt("new_file")


