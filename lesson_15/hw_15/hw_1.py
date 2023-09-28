"""
Вам необходимо написать скрипт на языке Python, который будет категоризировать письма, представленные в формате CSV.
Вам будет отправлен CSV-файл с перемешанными обезличенными письмами из разделов:
Security, Refunds, Troubleshooting, Account, Advertising and Collaboration, Limits, Payments, Features.

---

Требования:

1. Вам нужно разработать скрипт, который будет считывать содержимое CSV-файла и категоризировать каждое письмо
в соответствии с его содержимым.
Категория должна быть определена на основе ключевых слов, содержащихся в тексте письма.
2. Проанализируйте содержимое и выявите зависимости.
3. Создайте словарь с ключевыми словами для каждой категории.
4. Скрипт должен открывать CSV-файл,
считывать каждое письмо и проверять его содержимое на наличие ключевых слов для каждой категории.
5. Письмо должно быть отнесено к одной или нескольким категориям,
если оно содержит соответствующие ключевые слова и корни к ним.
6. Результаты категоризации должны быть сохранены в новом CSV-файле или выведены на экран в удобочитаемом формате.
7. Обратите внимание, что ключевые слова должны быть регистронезависимыми.
8. Дополнительным плюсом будет реализация обработки исключений,
чтобы скрипт не завершался с ошибкой при некорректной структуре CSV-файла или отсутствии файла.

---

### Вариант 1:
Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной строки с передачей параметров.

### Вариант 2:
https://github.com/bettercallvlad/test_task_python, задание с каникул,
но нужно добавить логирование несортированных сообщения и запуск из терминала.

Данная промежуточная аттестация оценивается по системе "зачет" / "не зачет"

"Зачет" ставится, если Слушатель успешно выполнил задание.
"Незачет" ставится, если Слушатель не выполнил задание.

### Критерии оценивания:
1 - Слушатель написал корректный код для задачи,
добавил к ним логирование ошибок и полезной информации.
"""

import csv
import logging

SECTIONS = dict(SECURITY=['работ', 'серви'],
                REFUNDS=['верну', 'возвр', 'деньг'],
                TROUBLESHOOTING=['пробл', 'ошибк', 'непра', 'забыл', 'баг'],
                ACCOUNT=['аккау', 'учетн', 'подпи', 'автор', 'логин'],
                ADVERTISING_AND_COLLABORATION=['сотру', 'рекла'],
                LIMIT=['лимит', 'огран', 'увели'],
                PAYMENTS=['плате', 'оплат', 'средс'],
                FEATURES=['функц'])


def logger():
    logging.basicConfig(filename="log.log", encoding='utf-8', level=logging.INFO, format="%(message)s")


def sorter(rows: list, selections: dict):
    """
    Вам необходимо написать скрипт на языке Python, который будет категоризировать письма, представленные в формате CSV.
    Вам будет отправлен CSV-файл с перемешанными обезличенными письмами из разделов:
    Security, Refunds, Troubleshooting, Account, Advertising and Collaboration, Limits, Payments, Features.
    """
    logger()
    for key, items in selections.items():
        dictor = []
        for number, message in rows:
            word = [word[:5].lower() for word in message[0].split()]

            if set(word) & set(items):
                if [number, message] not in dictor:

                    dictor.append({"number": str(number),
                                   "message": "".join(message)})

                    with open(f"{key}.csv", "w", encoding="utf-8", newline="") as file:
                        fieldnames = ['number', 'message']

                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        for line in dictor:
                            writer.writerow(line)
            else:
                error_msg = f"{number} - {''.join(message)} \n"
                logging.info(msg=error_msg)


with open("user_support_letters.csv", "r", encoding="utf-8") as f:
    data = []
    for num, row in enumerate(csv.reader(f), start=1):
        data.append([num, row])

sorter(data, SECTIONS)

if __name__ == '__main__':
    sorter(data, SECTIONS)
