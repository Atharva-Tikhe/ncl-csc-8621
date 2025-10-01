import datetime

class Car:
    TOP_SPEED = 100

    def __init__(self, year, make):
        if year is not None:
            self.year = year
        if make is not None:
            self.make = make

        self.__color = ""
        self.__category = ""
        self.speed = 0

    def __calculate_age(self):


    def __str__(self):
        return f"Car({self.year}, {self.make}, {self.get_color()}, {self.get_category()})"

    def accelerate(self):
        if self.speed < Car.TOP_SPEED:
            self.speed += 5
        else:
            pass

    def brake(self):
        if not self.speed == 0:
            self.speed -= 5

    def get_speed(self):
        return self.speed

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_category(self):
        return self.__category

    def set_category(self, category):
        self.__category = category




