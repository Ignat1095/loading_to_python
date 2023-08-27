# ### Задание №5
# 📌Напишите функцию, которая ищет json файлы в указанной директории и
# сохраняет их содержимое в виде одноимённых pickle файлов.
import json
import pickle
import os

__all__ = ["json_to_pickle"]


def json_to_pickle(directory: str = "seminar"):
    new_dir = os.getcwd()
    os.chdir("../")
    files = list(filter(lambda x: ".json" in x, os.listdir()))
    for file in files:
        file_name, *_ = file.split(".")

        with (open(file, 'r', encoding='utf-8')as source,
              open(f"{new_dir}\\{file_name}.pickle", 'wb') as res):
            data = json.load(source)
            pickle.dump(data, res)

        with open(f"{new_dir}\\{file_name}.pickle", 'rb') as res:
            file = pickle.load(res)
            for item in file:
                print(item)


if __name__ == "__main__":
    json_to_pickle()
