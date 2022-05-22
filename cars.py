import random
from car import Car


class Cars:
    def __init__(self):
        self.cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            car = Car()
            self.cars.append(car)
        self.move()

    def move(self):
        for car in self.cars:
            car.move()

    def update_speed(self):
        for car in self.cars:
            car.move_speed += 5
