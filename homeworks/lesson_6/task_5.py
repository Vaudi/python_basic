"""
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
"""

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(self.title)


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(self.title, 'пишет')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(self.title, 'рисует')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(self.title, 'выделяет')


itm0 = Stationery('Запуск отрисовки')
itm1 = Pen('Ручка')
itm2 = Pencil('Карандаш')
itm3 = Handle('Маркер')
itm0.draw()
itm1.draw()
itm2.draw()
itm3.draw()