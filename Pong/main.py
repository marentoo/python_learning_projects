from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black"); screen.title("PONG")
screen.tracer(0)


player1 = Paddle(350)
player2 = Paddle(-350)

scoreboard = Scoreboard()


ball = Ball()

screen.listen()

screen.onkey(player1.move_up, "Up")
screen.onkey(player1.move_down, "Down")
screen.onkey(player2.move_up, "w")
screen.onkey(player2.move_down, "s")



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()


    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with the paddle
    if ball.distance(player1) < 50 and ball.xcor() > 320 or ball.distance(player2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect player1 misses
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()

    #detect player2 misses
    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_point()

screen.exitonclick()