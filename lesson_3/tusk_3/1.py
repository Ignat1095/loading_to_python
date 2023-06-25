# ✔Три друга взяли вещи в поход.
# Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# ✔Какие вещи взяли все три друга
# ✔Какие вещи уникальны, есть только у одного друга.
# ✔Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.

friends_dict = {"Антон": ["спальник", "палатка", "лопата"],
                "Кирилл": ["спальник", "палатка", "решетка"],
                "Сергей": ["спальник", "мангал", "шашлык"],
                "Петя": ["спальник", "шашлык", "решетка"]}


def all_items(f_dict) -> dict:
    items_dict = {}
    all_item = sum(f_dict.values(), [])
    for i in all_item:
        items_dict[i] = items_dict.get(i, 0) + 1
    return items_dict


def unique_one(inventory: dict[str, list]) -> str:
    unique_list = []
    for friend, value in inventory.items():
        my_inventory = set(value)
        for cur_friend, cur_values in inventory.items():
            if friend != cur_friend:
                my_inventory.difference_update(cur_values)
        unique_list.append((friend, my_inventory if my_inventory else {'Уникальных вещей нет'}))

    return "Список уникальных вещей: \n" + '\n'.join([f'{items[0]}: 'f'{", ".join([item for item in list(items[1])])}'
                                                     for items in unique_list])


def all_except_one(inventory: dict[str, list]) -> str:
    result = {}
    all_item = set(all_items(friends_dict).keys())
    # print(all_item)
    for name, items in inventory.items():
        cur_inventory = all_item.copy()
        for cur_name, cur_items in inventory.items():
            if name != cur_name:
                cur_inventory.intersection_update(set(cur_items))
            result[name] = cur_inventory.difference(items)
        return "Вещи, которые есть у все, кроме: \n" + \
               "\n".join(f'{name}: {", ".join([item for item in items])}' for name, items in result.items())


print(f'Список всех вещей: {all_items(friends_dict)}')
print()
print(unique_one(friends_dict))
print()
print(all_except_one(friends_dict))







