"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

while True:
    user_number = input ('Введите целое положительное число')
    if user_number.isdigit():
        user_number = int (user_number)
        break
    else:
         print ('Некорректный ввод, введите целое положительное число')

result = 0
while user_number and result !=9:
    tmp=user_number % 10
    if tmp > result:
        result = tmp
    user_number //= 10
print (result)
