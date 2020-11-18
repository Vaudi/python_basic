"""
Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
"""
first_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

second_list = [first_list[i] for i in range(1, len(first_list) - 1) if first_list[i] > first_list[i-1]]
print(second_list)
