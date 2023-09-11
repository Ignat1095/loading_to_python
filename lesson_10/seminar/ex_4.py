# ### Задание №4
# 📌Создайте класс Сотрудник.
# 📌Воспользуйтесь классом человека из прошлого задания.
# 📌У сотрудника должен быть:
#
# * шестизначный идентификационный номер
# * уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

from ex_3 import Info


class Employee(Info):

    def __init__(self, fio: str, age: int, ids):
        super().__init__(fio, age)
        self.id = f"{ids:06}"
        self.access_level = sum(list(map(int, str(self.id)))) % 7

old_men = Employee("петрович стас", 67, 5136)
print(f"{old_men.fio = }")
print(f"{old_men.get_age() = }")
print(f"{old_men.id = }")
print(f"{old_men.access_level = }")

