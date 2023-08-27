# ### Задание №4
# 📌Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# 📌Дополните id до 10 цифр незначащими нулями.
# 📌В именах первую букву сделайте прописной.
# 📌Добавьте поле хеш на основе имени и идентификатора.
# 📌Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# 📌Имя исходного и конечного файлов передавайте как аргументы функции.
import json


def csv_to_json(csv_file: str, json_file: str):
    with open(csv_file, 'r', encoding='utf-8') as csv_f:
        data = csv_f.read().split()
        res = []
        data.pop(0)
        for i in data:
            level, id, name = i.split(",")
            res.append({"level": level,
                        # "id": id.zfill(10),
                        "id": f"{int(id):010}",
                        "name": name.capitalize(),
                        "hash": hash(id+name)})

    with open(json_file, 'w', encoding="utf-8") as json_f:
        json.dump(res, json_f, indent=4)


if __name__ == "__main__":
    csv_to_json("ex_2.csv", "ex_4.json")
