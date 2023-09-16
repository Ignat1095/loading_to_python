# ### Задание №2
# 📌Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# 📌При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
# 📌list-архивы также являются свойствами экземпляра

class Archive:
    """
    documentation
    """
    archive = None

    def __init__(self, num: int, text: str):
        self.num = num
        self.text = text

    def __new__(cls, *args):
        if cls.archive:
            cls.archive.old_text.append(cls.archive.text)
            cls.archive.old_num.append(cls.archive.num)
        else:
            cls.archive = super().__new__(cls)
            cls.archive.old_text = []
            cls.archive.old_num = []
        return cls.archive

print(Archive.__doc__)

a = Archive(123, "Sasha go to road")
print(Archive.archive.old_num)
print(Archive.archive.old_text)

b = Archive(124, "Nikita ead bread")
print(Archive.archive.old_num)
print(Archive.archive.old_text)

c = Archive(125, "Kitty kat")
print(Archive.archive.old_num)
print(Archive.archive.old_text)