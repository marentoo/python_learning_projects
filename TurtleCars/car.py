from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "blue", "purple","green"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        print("instantiation of object: car list")
        self.speed = STARTING_MOVE_DISTANCE
    def create_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_y = random.randint(-250, 250)
            new_car.goto(290, new_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def level_up(self):
        self.speed += MOVE_INCREMENT