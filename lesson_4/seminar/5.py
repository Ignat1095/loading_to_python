# ✔Функция принимает на вход три списка одинаковой длины:
# ✔имена str,
# ✔ставка int,
# ✔премия str с указанием процентов вида «10.25%».
# ✔Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# ✔Сумма рассчитывается как ставка умноженная на процент премии.


def premia(names:list[str], stavka:list[str], persents:list[str]):
    dict_of_premia = {}
    for index, name in enumerate(names):
        dict_of_premia[name] = stavka[index] * float(persents[index][0:-1]) / 100
    return dict_of_premia

names = ['aaa', 'bbb', 'ccc']
stavka = [1000, 2000, 3000]
persents = ['10.23', '10.23', '10.23']

print(premia(names, stavka, persents))