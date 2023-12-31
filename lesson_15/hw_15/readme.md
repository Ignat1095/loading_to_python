## Разработка скрипта для категоризации пользовательских запросов
***
### Задание:
Вам необходимо написать скрипт на языке Python, который будет категоризировать письма, представленные в формате CSV.  
Вам будет отправлен CSV-файл с перемешанными обезличенными письмами из разделов:  
Security, Refunds, Troubleshooting, Account, Advertising and Collaboration, Limits, Payments, Features.

---

Требования:

1. Вам нужно разработать скрипт, который будет считывать содержимое CSV-файла и категоризировать каждое письмо в соответствии с его содержимым. Категория должна быть определена на основе ключевых слов, содержащихся в тексте письма.
2. Проанализируйте содержимое и выявите зависимости.
3. Создайте словарь с ключевыми словами для каждой категории. 
4. Скрипт должен открывать CSV-файл, считывать каждое письмо и проверять его содержимое на наличие ключевых слов для каждой категории.
5. Письмо должно быть отнесено к одной или нескольким категориям, если оно содержит соответствующие ключевые слова и корни к ним. 
6. Результаты категоризации должны быть сохранены в новом CSV-файле или выведены на экран в удобочитаемом формате.
7. Обратите внимание, что ключевые слова могут быть регистронезависимыми, то есть их наличие в письме должно быть определено без учета регистра.
8. Дополнительным плюсом будет реализация обработки исключений, чтобы скрипт не завершался с ошибкой при некорректной структуре CSV-файла или отсутствии файла.
 
---

## Урок 15. Обзор стандартной библиотеки Python

### Вариант 1: 
Возьмите любые 1-3 задания из прошлых домашних заданий.  
Добавьте к ним логирование ошибок и полезной информации.  
Также реализуйте возможность запуска из командной строки с передачей параметров. 

### Вариант 2: 
https://github.com/bettercallvlad/test_task_python, задание с каникул, 
но нужно добавить логирование несортированных сообщения и запуск из терминала.
---

Данная промежуточная аттестация оценивается по системе "зачет" / "не зачет":  
**"Зачет"** ставится, если Слушатель успешно выполнил задание.  
**"Незачет"** ставится, если Слушатель не выполнил задание.

#### Критерии оценивания:
1 - Слушатель написал корректный код для задачи,  
добавил к ним логирование ошибок и полезной информации.