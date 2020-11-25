"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.Задачу можно усложнить,
реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
import time
from itertools import cycle

class TrafficLight:
    __modes = (('Красный', 7), ('Желтый', 2), ('Зеленый', 5))
    __light_start = 0
    __next_light = 0

    def __init__(self):
        self.__color = self.__modes[0][0]
        self.__tic()

    def running(self):
        prew_color = None
        while True:
            self.__tic()
            if prew_color != self.__color:
                prew_color = self.__color
                print(self.__color)

    def __tic(self):
        if self.__light_start + dict(self.__modes)[self.__color] <= time.time():
            self.__color, self.__light_start = self.__modes[self.__next_light][0], time.time()
            self.__next_light = self.__next_light + 1 if len(self.__modes) > self.__next_light + 1 else 0

    def color(self):
        self.__tic()
        return self.__color

    def set_mode(self, color):
        if self.__modes[self.__next_light][0] != color:
            raise ValueError('Нельзя включить этот цвет')
        self.__tic()

if __name__ == '__main__':
    lighter = TrafficLight()
    lighter.running()