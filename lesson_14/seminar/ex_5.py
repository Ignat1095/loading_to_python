"""
### Задание №5
📌На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину, а также
вычисляющую периметр, площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр.
📌Напишите 3-7 тестов unittest для данного класса.
"""

from lesson_10.seminar.ex_2 import Rectangle
import unittest


class TestRectangleText(unittest.TestCase):
    def setUp(self):
        self.r1 = Rectangle(length=2, width=3)
        self.r2 = Rectangle(length=2)
        self.r3 = Rectangle(length=2)

    def test_step_1(self):
        self.assertEqual(self.r2, self.r3)

    def test_step_2(self):
        self.assertTrue(self.r3 == self.r2, "Сравнение работает не корректно")

if __name__ == '__main__':
    unittest.main()