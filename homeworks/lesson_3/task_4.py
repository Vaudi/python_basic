"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

"""

def my_func(x, y):

    result1 = x ** y
    var = x
    for _ in range(1, abs(y)):
        x *= var
    result2 = 1 / x
    return result1, result2

def num_input(arg, asc, type_arg):

    num = 0
    while num * arg <= 0:
        try:
            num = num if num * arg > 0 else type_arg(input(asc))
        except ValueError:
            print('Ошибка ввода')
    return num

x = num_input(1, 'Введите положительное число: ', float)
y = num_input(-1, 'Введите целое отрицательное число: ', int)
print(my_func(x, y))