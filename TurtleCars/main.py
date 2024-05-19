from turtle import Turtle, Screen
import time
from player import Player
from car import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    ##detect collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 15:
            print("Collision")
            game_is_on = False
            scoreboard.game_over()

    ## detect collision with finnish line
        if player.ycor() > 295:
            print("finish line")
            player.reset_position()
            car_manager.level_up()
            scoreboard.increase_level()

screen.exitonclick()
