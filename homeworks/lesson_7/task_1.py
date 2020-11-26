"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
"""

from itertools import zip_longest


class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        result = ''
        for itm in self.data:
            result += f'| {" | ".join(map(str, itm))} | \n'
        return result

    def __add__(self, other):
        res = []
        for row_dat, row_oth in list(zip_longest(self.data, other.data, fillvalue=0)):
            row = []
            for el_dat, el_oth in list(zip_longest(row_dat, row_oth, fillvalue=0)):
                row.append(el_dat + el_oth)
            res.append(row)
        return Matrix(res)


a = Matrix([[1, 2, 3], [5, 6], [7, 8, 9]])
b = Matrix([[3, 1], [6, 5, 4], [9, 8]])
print(a)
print(b)

print(a + b)