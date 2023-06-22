# ✔Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s
# (кроме переменной из одной буквы s) на None.
# ✔Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
a = "qwerty"
bs = 123
cs = True
s = 0


for key, value in globals().copy().items():
    if not key.startswith('__'):
        print(key, ' = ', value)
        if key.endswith('s'):
            if len(key) > 1:
                new_name = key[:-1]
                globals()[new_name] = None
            else:
                globals()[key] = globals().get(key)
print()
for key, value in globals().copy().items():
    if not key.startswith('__'):
        print(key, ' = ', value)

print(f'{b = }')
print(f'{c = }')
