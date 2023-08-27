# 📌Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# * Для дочерних объектов указывайте родительскую директорию.
# * Для каждого объекта укажите файл это или директория.
# * Для файлов сохраните его размер в байтах,
# а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
#
#     Пример:
#     test/users/names.txt
#     Результат в json для names.txt:
#     {
#     "name": names.txt
#     "parent": users,
#     "type": "file"
#     "size": 4096
#     }
import json
import csv
import pickle
import os


def what_in_directory(directory, res_directory):
    result = []
    for parent, dirs, files in os.walk(directory):
        folder_size = 0
        for file in files:
            name = os.path.join(parent, file)
            size = os.path.getsize(name)
            folder_size += size
            result.append({"parent": parent.split("\\")[-1],
                           "name": name.split("\\")[-1],
                           "type": "file",
                           "size": size})
        result.append({"parent": os.path.dirname(parent).split("\\")[-1],
                       "name": parent.split("\\")[-1],
                       "type": "folder",
                       "size": folder_size})

    with open(f"{res_directory}\\json_type.json", 'w', encoding='UTF-8') as json_f:
        json.dump(result, json_f, indent=4, ensure_ascii=False)

    with open(f"{res_directory}\\csv_type.csv", 'w', encoding='UTF-8', newline="") as csv_f:
        fieldnames = list(map(str, result[0].keys()))
        csv_writer = csv.DictWriter(csv_f, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(result)

    with open(f"{res_directory}\\pickle_type.pickle", 'wb') as pickle_f:
        pickle.dump(result, pickle_f)

if __name__ == "__main__":
    what_in_directory("D:\\Учеба_GeekBrains\\4 Python\\loading_to_python\\lesson_8\\seminar", os.getcwd())
