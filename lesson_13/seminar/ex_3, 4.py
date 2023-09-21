"""
### Задание №3
📌Создайте класс с базовым исключением и дочерние классы - исключения:
* ошибка уровня,
* ошибка доступа.

### Задание №4
📌Вспоминаем задачу из семинара 8 про сериализация данных,
где в бесконечном цикле запрашивали имя, личный идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
📌Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
📌Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.
"""
import json


class MyException(Exception):
    pass


class MyExceptionAccess(MyException):
    pass


class MyExceptionLevel(MyException):
    pass


class User:
    def __init__(self, user_id: int, level: int, user_name: str):
        self._user_id = user_id
        self.level = level
        self.user_name = user_name

    @staticmethod
    def load(file_name):
        with open(f"{file_name}.json", "r", encoding="utf-8") as j_file:
            data = json.load(j_file)
        users = set()
        for user in data:
            users. add(User(*user.values()))
        return users

    def __eq__(self, other):
        return self.user_name == other.user_name and \
               self._user_id == other._user_id

    def __hash__(self):
        return int(self._user_id)

    def __str__(self):
        return f"{self.level = }, {self._user_id = }, {self.user_name}"

peoples = User(level=1, user_id=1, user_name="who i am")
# print(peoples.load("ex_3"))
# print(peoples)


"""
### Задание №5  
📌Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:  
📌загрузка данных (функция из задания 4)  
📌вход в систему - требует указать имя и id пользователя.  
Для проверки наличия пользователя в множестве используйте магический метод проверки на равенство пользователей.  
Если такого пользователя нет, вызывайте исключение доступа.  
А если пользователь есть, получите его уровень из множества пользователей.  
📌добавление пользователя.  
Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.
"""


class Project:
    def __init__(self):
        self.users = User(level=1, user_id=1, user_name="who i am").load("ex_3")
        self.entered_user = None

    def reload_users(self):
        self.users = User(level=1, user_id=1, user_name="who i am").load("ex_3")

    def enter(self, id_: int, name: str):
        that_user = User(level=None, user_id=id_, user_name=name)
        if that_user not in self.users:
            raise MyExceptionAccess
        for i in self.users:
            if i == that_user:
                self.entered_user = i

    def add_user(self, id_, level, name):
        if self.entered_user.level < level:
            raise MyExceptionLevel
        self.users.add(User(id_, level, name))


if __name__ == "__main__":
    proj = Project()
    proj.enter(2, "Mary")
    proj.add_user("124565", 1, "Igor")
    print(proj.users)