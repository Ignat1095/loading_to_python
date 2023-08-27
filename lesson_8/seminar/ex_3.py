### Задание №3
# 📌Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
import json
import csv


def json_to_csv(file_json: str, file_csv: str):
    with open(file_json, 'r', encoding="utf-8") as f_j:
        data: dict = json.load(f_j)

    rows = []
    for level, users in data.items():
        for id, name in users.items():
            rows.append({"level": level,
                         "id": id,
                         "name": name})

    with open(file_csv, "w", encoding="utf-8", newline="") as csv_file:
        filenames = ["level", "id", "name"]

        csv_writer = csv.DictWriter(csv_file, fieldnames=filenames)

        csv_writer.writeheader()
        csv_writer.writerows(rows)


if __name__ == "__main__":
    json_to_csv("ex_2.json", "ex_2.csv")
