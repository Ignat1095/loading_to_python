# ### Задание №2
# 📌Напишите функцию, которая в бесконечном цикле запрашивает:

# имя,
# id,
# уровень доступа (от 1 до 7).

# 📌После каждого ввода добавляйте новую информацию в JSON файл.
# 📌Пользователи группируются по уровню доступа.
# 📌Идентификатор пользователя выступает ключом для имени.
# 📌Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# 📌При перезапуске функции уже записанные в файл данные должны сохраняться.
import json


def unique_id(data: dict, id: str) -> bool:
    for item in data.keys():
        if id in item:
            return False
    return True


def json_file(new_file: str):
    while True:
        name = input("name: ")
        id = input("id: ")
        level = input("level: ")

        try:
            with open(new_file, 'r', encoding="utf-8") as file_r:
                result: dict = json.load(file_r)
        except:
            result: dict = {str(i): {} for i in range(1, 8)}

        if unique_id(result, id):
            result[level].update({id: name})
            print(f"Этот ID ({id} занят)")
        else:
            continue

        with open(new_file, 'w', encoding="utf-8") as file_a:
            json.dump(result, file_a, indent=4)


# json_file("ex_2.json")


if __name__ == "__main__":
    json_file("ex_2.json")
