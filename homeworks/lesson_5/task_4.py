"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.
"""

my_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
new_dict = {}
try:
    with open('task_4_file.txt', 'r', encoding='UTF-8') as file:
        for line in file:
            var_key = list(line.split())[0]
            new_dict[my_dict[var_key]] = list(line.split())[2]
except FileNotFoundError:
    print('файл не существует')
with open('task_4_new_file.txt', 'w', encoding='UTF-8') as new_f:
    for key, val in new_dict.items():
        new_f.writelines(f'{key} - {val}\n')