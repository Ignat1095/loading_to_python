# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.
from itertools import chain, combinations

item_dict = {"Палатка": 5,
             "Спальник": 3,
             "Веревки": 2.5,
             "Скальные крючья": 4,
             "Фотик": 1.5,
             "Штатив": 2,
             "GPS": 1}
capacity = 15


def best_value(items: dict[str, float]) -> list[str, float]:
    item_list = sorted((list(items.items())), key=lambda x: x[1], reverse=True)
    return item_list


def sorted_weight(weight_item: list[str, float], weight_limit: int) -> str:
    backpack_item = []
    max_weight = weight_limit
    for item in weight_item:
        if item[1] <= max_weight:
            backpack_item.append(item)
            max_weight -= item[1]
    max_length = max([len(x[0]) for x in backpack_item])
    result = [f"В рюкзак с max весом в {weight_limit} у.е. мы можем положить: "]
    for i, item in enumerate(backpack_item, 1):
        result.append(f"{i}. {item[0]:.<{max_length}} {item[1]}")
    return '\n'.join(result)

print(sorted_weight(best_value(item_dict), capacity))

print("\nДалее решение преподавателя\n")


def max_cargo(inventory: dict[str, float], weight_limit: int) -> str:
    backpack = [[], 0]
    for item, weight in inventory.items():
        if backpack[1] + weight <= weight_limit:
            backpack[0].append(item)
            backpack[1] += weight
        else:
            break
    result = [f"В рюкзак с max весом в {weight_limit} у.е. мы можем положить: \n"]
    for item in backpack:
        result.append(f" {item}")
    return ''.join(result)

# print(max_cargo(item_dict, capacity))


def powerset(inventory: dict[str, float]):
    return chain.from_iterable(combinations(inventory, r) for r in range(1, len(inventory) + 1))


def all_options(inventory: dict[str, float], weight_limit: int):
    result = []
    for cur_option in powerset(list(inventory)):
        weight = 0
        for item in cur_option:
            weight += inventory.get(item)
        if (capacity - min(inventory.values())) <= weight <= weight_limit:
            result.append((cur_option, weight))
    return result


# print(all_options(item_dict, capacity))
for option in all_options(item_dict, capacity):
    print(option)



