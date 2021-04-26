class Car:
    def __init__(self, marka, model, ege, speed=0):
        self.__marka = marka
        self.__model = model
        self.__ege = ege
        self.__speed = speed
    def speed_plus(self):
        self.speed += 5
    def speed_minus(self):
        self.speed -= 5
    def speed_stop(self):
        self.speed = 0
    def speed_print(self):
        print(self.speed)
    def speed_znak(self):
        self.speed *= -1
car1 = Car('mers', 600, 20, -5)
car1.speed_znak()
car1.speed_print()

