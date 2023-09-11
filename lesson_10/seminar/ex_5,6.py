# ### Задание №5
# 📌Создайте три (или более) отдельных классов животных. Например: рыбы, птицы и т.п.
# 📌У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# 📌Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

# ### Задание №6
# 📌Доработайте задачу 5.
# 📌Вынесите общие свойства и методы классов в класс Животное.
# 📌Остальные классы наследуйте от него.
# 📌Убедитесь, что в созданные ранее классы внесены правки.

class Animal:
    def __init__(self,
                 name: str,
                 age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return self.age, self.age


class Dog(Animal):
    def __init__(self,
                 name: str,
                 age: int,
                 color: str,
                 breed: str):
        super().__init__(name, age)
        self.color = color
        self.breed = breed

    def __str__(self):
        return f"{self.name}, {self.age}, {self.color}, {self.breed}"


dog1 = Dog("Песик", 3, "бурый", "стафор")
print(dog1)
dog2 = Dog("зверь", 5, "рыжий", "двор")
print(dog2)
