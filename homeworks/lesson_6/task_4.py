"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

class Car:
    def __init__(self, color: str, name: str, is_police: bool = False):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Car is go')

    def stop(self):
        print('Car stopped')

    def turn(self, direction):
        if direction in ('left', 'right'):
            print(f'Car turn to {direction}')
        else:
            raise ValueError('direction values  left, right only')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):

    def __init__(self, color, name):
        super().__init__(color, name)

    def show_speed(self):
        if self.speed > 60:
            print('Overspeed')
        super().show_speed()


class SportCar(Car):
    def __init__(self, color, name):
        super().__init__( color, name)


class WorkCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)

    def show_speed(self):
        if self.speed > 40:
            print('Overspeed')
        super().show_speed()


class PoliceCar(Car):
    def __init__(self, color, name,):
        super().__init__(color, name, True)


if __name__ == '__main__':
    police = PoliceCar('White', 'Ford')
    town = TownCar('Blue', 'Volvo')