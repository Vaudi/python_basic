"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

"""
from sys import argv

def salary(hour: float, price: float, bonus: float,) -> float:
    return hour * price + bonus

try:
    _, hour, price, bonus, *_ = argv
    result = float(hour) * float(price) + float(bonus)
    print(result)
except ValueError as e:
    print('Ошибка ввода')
    print(e)

