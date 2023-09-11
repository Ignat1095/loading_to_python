# ### Задание №3
# 📌Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
# 📌У класса должны быть методы:
#
# * birthday для увеличения возраста на год,
# * full_name для вывода полного ФИО и т.п. на ваш выбор.
#
# 📌Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.

class Info:
    def __init__(self, fio: str, age: int):
        self.fio = fio.title()
        self.__age = age

    def birthday(self):
        self.__age += 1

    def get_age(self):
        return self.__age

    def __str__(self):
        return f"{self.fio.title()}"

r1 = Info("иван неиванович илииван", 34)

print(r1)
print(r1.get_age())
# print(r1.__age)
r1.birthday()
print(r1.get_age())
