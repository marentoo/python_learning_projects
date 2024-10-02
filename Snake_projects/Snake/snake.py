from turtle import Turtle, Screen

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:

    def __init__(self):
        print("object: snake instantiated!")
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_seg = Turtle("square")
        new_seg.color("white", "white")
        new_seg.penup()
        new_seg.goto(position)
        self.body.append(new_seg)

    def extend_snake(self):
        self.add_segment(self.body[-1].position())

    def move(self):
        #last segment should become middle segment | and middle segment should become first | and first should go to dest
        for segment_num in range(len(self.body) - 1, 0, -1):
            new_xcor = self.body[segment_num - 1].xcor()
            new_ycor = self.body[segment_num - 1].ycor()
            self.body[segment_num].goto(new_xcor, new_ycor)
        self.head.forward(MOVE_DISTANCE)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)