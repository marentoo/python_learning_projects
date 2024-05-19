from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)

scoreboard = Scoreboard()
apple = Food()
snake = Snake()

screen.listen()
screen.onkey(snake.move_right, "d")
screen.onkey(snake.move_left, "a")
screen.onkey(snake.move_up, "w")
screen.onkey(snake.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #detect collision with food
    if snake.head.distance(apple) < 15:
        apple.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    #detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        scoreboard.game_over()
        game_is_on = False

    #detect collision with tail
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 5:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
