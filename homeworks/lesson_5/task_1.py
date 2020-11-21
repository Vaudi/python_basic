"""
Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

import os

file_path = os.path.join(os.path.dirname(__file__), 'task_1_file.txt')

print('Для выхода введите пустую строку.')

with open(file_path, 'w', encoding='UTF-8') as file:
    while True:
        user_data = input('Введите данные\n')
        if not user_data:
            break
        file.write(f'{user_data}\n')