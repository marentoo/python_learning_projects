from turtle import Turtle, Screen

ALIGNEMENT = "center"
FONT = ("Comic Sans MS", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.shape()
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNEMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNEMENT,font=FONT)
