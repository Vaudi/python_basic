"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

while True:
    user_number = input ('Введите целое число\n')
    if user_number.isdigit():
        break
    print ('Некорректный ввод, введите целое число')

result = int (user_number) + int (user_number*2) + int (user_number*3)
print (result)