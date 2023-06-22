# Написать программу, которая будет выводить в консоль ёлочку заданной высоты.

hight = 20
body = "*"
segment = 1

for i in range(hight):
    result = body * segment
    indent = ' ' * (hight - i)
    segment += 2
    print(indent, result)

