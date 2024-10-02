from turtle import Turtle, Screen
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color("red", "red")
        self.speed("fastest")
        self.goto(random.randint(-280, 260), random.randint(-280, 260))
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-280, 260), random.randint(-280, 260))
