"""
### Задание №6
📌На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
📌Напишите 3-7 тестов pytest для данного проекта.
📌Используйте фикстуры.

"""
import pytest
from lesson_10.seminar.ex_2 import Rectangle


@pytest.fixture()
def r1():
    return Rectangle(length=2)


@pytest.fixture()
def r2():
    return Rectangle(length=2, width=4)


@pytest.fixture()
def r3():
    return Rectangle(length=2)


def test_step_1(r1, r3):
    assert r1 == r3


def test_step_2(r1, r2):
    assert r1 != r2


if __name__ == '__main__':
    pytest.main(["--vv"])