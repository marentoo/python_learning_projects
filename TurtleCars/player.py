from turtle import Turtle

START_POSITION = (0, -250)
MOVE_DISTANCE = 20
FINISH_LINE = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        print("instantiation of object: player")
        self.shape("turtle")
        self.shapesize(1.2, 1.2)
        self.color("yellow", "black")
        self.penup()
        self.goto(START_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(START_POSITION)
