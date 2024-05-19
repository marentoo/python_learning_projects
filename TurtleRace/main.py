from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle win the race? Enter a color: ")
colors = ["red", "orange", "green", "yellow", "blue", "purple"]
turtle_list = []

x = -230
y = -150
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed("fastest")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x, y)
    y += 60
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"Congrats! {winning_turtle} won.")
            else:
                print(f"You lose! {winning_turtle} won.")
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
