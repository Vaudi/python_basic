"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def div(*args):

    try:
        arg1 = int(input("Введите делимое"))
        arg2 = int(input("Введите делитель"))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "На ноль делить нельзя"

    return res

print(f'Результат  {div()}')
