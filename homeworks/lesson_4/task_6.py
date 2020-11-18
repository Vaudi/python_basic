"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
"""
from itertools import count
from itertools import cycle

i = int(input('Введите стартовое число:'))
for j in count(i):
    if j >= 100:
        break
    else:
        print(j)

print ('-' * 20)

m = 0
for n in cycle([11, 22, 33, 44, 55]):
    if m >= 10:
        break
    else:
        print(n)
    m += 1