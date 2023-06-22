# Написать программу, которая выводит в консоль таблицу умножения "как на тетрадках"


for i in range(2, 11):

    for j in range(2, 6):
        print(f'{j}  x {i:>2} = {i * j:>2}', end=' '*5)
    print()

print()

for i in range(2, 11):

    for j in range(6, 10):
        print(f'{j}  x {i:>2} = {i * j:>2}', end=' '*5)
    print()
