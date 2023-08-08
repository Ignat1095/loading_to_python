# Основная задача: Задача:
# Расчет финансовых показателей портфеля акций Описание задачи:
# Вы являетесь инвестором и хотите создать программу для расчета нескольких финансовых показателей вашего портфеля акций.
# Создайте модуль Python под названием "portfolio.py", который будет содержать функции для выполнения следующих операций:
#
# Расчет общей стоимости портфеля акций:
# Функция calculate_portfolio_value(stocks: dict, prices: dict) -> float принимает два аргумента:
# stocks - словарь, где ключами являются символы акций (например, "AAPL" для Apple Inc.),и
# значениями - количество акций каждого символа.
# Prices - словарь, где ключами являются символы акций, а значениями - текущая цена каждой акции.
# Функция должна вернуть общую стоимость портфеля акций на основе количества акций и их текущих цен.
#
# Пример: Пришло
# stocks = {"AAPL": 10, "SBER": 5, "SPCE": 8}
# prices = {"AAPL": 195.0, "SBER": 268.0, "SPCE": 4,14}
# Вышло: 16410,25
#
# Расчет доходности портфеля:
# Функция calculate_portfolio_return(initial_value: float, current_value: float) -> float принимает два аргумента:
# initial_value - начальная стоимость портфеля акций.
# current_value - текущая стоимость портфеля акций. Функция должна вернуть процентную доходность портфеля.
# Пример:
# Пришло: 10000.0, 15000.0
# Вышло: 50%
#
# Определение наиболее прибыльной акции:
# Функция get_most_profitable_stock(stocks: dict, prices: dict) -> str принимает два аргумента:
# stocks - словарь с акциями и их количеством.
# prices - словарь с акциями и их текущими ценами.
# Функция должна вернуть символ акции (ключ), которая имеет наибольшую прибыль по сравнению с ее начальной стоимостью.
# Начальная стоимость - первый вызов calculate_portfolio_value,
# данные из этого вызова следует сохранить в защищенную переменную на уровне модуля.
# Пример:
# Пришло:
# stocks = {"AAPL": 10, "SBER": 5, "SPCE": 8}
# prices = {"AAPL": 195.0, "SBER": 268.0, "SPCE": 4,14}
# Вышло: MSFT
#
# Тестирование модуля:
#
# Напшите небольшую програму, которая импортирует модуль "portfolio.py" и демонстрирует использование всех трех функций.
# Создайте словари для акций и цен, запустите функции и выведите результаты.
# Примечание:
# В реальном мире вы можете использовать API для получения актуальных данных о ценах акций.
# В данной задаче можно использовать фиктивные данные для тестирования и обучения.
from typing import List, Any, Dict

stocks1 = dict(AAPL=10, SBER=20, SPCE=40)
prices1 = dict(AAPL=195.0, SBER=268.0, SPCE=50)

stocks2 = dict(AAPL=10, SBER=20, SPCE=40)
prices2 = dict(AAPL=195.0 * 1.05, SBER=268.0 * 0.95, SPCE=50 * 0.50)


def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    result = sum(map(lambda x, y: x * y, stocks.values(), prices.values()))
    return result


initial = calculate_portfolio_value(stocks1, prices1)
current = calculate_portfolio_value(stocks2, prices2)


# print(f'{initial = }')
# print(f'{current = }')


def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    return round(((current_value - initial_value) / initial_value) * 100, 2)


def stock_prise(stock: dict, prise: dict):
    for key, value in stock.items():
        stock[key] = value * prise[key]
    return stock


stock_prise_1 = stock_prise(stocks1, prices1)
stock_prise_2 = stock_prise(stocks2, prices2)



def get_most_profitable_stock(initial: dict, current: dict) -> dict[Any, Any]:
    for key, value in current.items():
        current[key] = value - initial[key]
    result = max(current, key=current.get)
    return result


print(f"Стоимость пакета акций = {calculate_portfolio_value(stocks1, prices1)} $")
print(f"Расчет доходности портфеля: {calculate_portfolio_return(initial, current)} %")
print(f'Наиболее прибыльная акция = {get_most_profitable_stock(stock_prise_1, stock_prise_2)}')
