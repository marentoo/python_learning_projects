from turtle import Turtle, Screen

DISTANCE = 30


class Paddle(Turtle):
    def __init__(self, x_pos):
        print("instantiation of the object: paddle")
        self.x_pos = x_pos
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(x_pos, 0)

    def move_up(self):
        new_y = self.ycor() + DISTANCE
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - DISTANCE
        self.goto(self.xcor(), new_y)
