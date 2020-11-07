"""
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

while True:
    proceeds = input ('Введите сумму выручки')
    if proceeds.isdigit():
        proceeds = int (proceeds)
        break
    print ('Некорректный ввод, введите число')

while True:
    costs = input ('Введите сумму издержек')
    if costs.isdigit ():
        costs = int (costs)
        break
    print ('Некорректный ввод, введите число')

fin_result = proceeds - costs

if fin_result > 0:
    ratio = proceeds / costs
    print (f'Ваша прибыль равна:{fin_result}\n Соотношение прибыли к выручке {ratio}')
    while True:
        staff = input('Введите число сотрудников')
        if staff.isdigit ():
            staff = int (staff)
            break
        print ('Некорректный ввод, введите число')
    profit_per_emp = fin_result / staff

    print (f'прибыль на одного сотрудника составляет: {profit_per_emp}')

elif not fin_result:
    print ('Прибыли и убытков нет')
else:
    print (f'Ваш убыток равен: {fin_result}')