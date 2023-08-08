# Задание 1
# Вспомните, какие модули вы проходили на курсе.
# Создайте файл, в котором вы импортируете встроенные в модуль функции под псевдонимами. (3-7 строк импорта).
import sys
from random import randint as rd
import math
from datetime import datetime as dt


print(any_digit := [rd(2, 20) for i in range(1, 20)])

print([round(math.pow(i, 2)) for i in range(2, 10)])

print(dt.now())


