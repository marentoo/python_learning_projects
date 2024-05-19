#!C:\mat\a1_praca-rozwoj\skill_i_wiedza\python_nauka\100_days_nauka\TurtleGraphics\.venv\Scripts\python.exe
import colorgram
import turtle
from turtle import Screen, Turtle, colormode
import random

def color_tuple_extraction(path, number_colors_extract):
    colors = colorgram.extract(path, num_colors)

    colors_list = []

    for i in range(number_colors_extract):
        single_color = colors[i]
        rgb_colors = single_color.rgb
        tuple_first = (rgb_colors[0], rgb_colors[1], rgb_colors[2])
        colors_list.append(tuple_first)

    return colors_list


def paint_row_of_dots():
    # paint dot and go left
    painter.dot(20, random.choice(final_color_list))
    for _ in range(10):
        painter.penup()
        painter.forward(50)
        painter.pendown()
        painter.dot(20, random.choice(final_color_list))


def go_up_one_level(start_position_x, start_position_y):
    # go up
    painter.left(90)
    painter.penup()
    painter.forward(50)
    painter.setx(start_position_x)
    start_position_y -= 10
    painter.right(90)


num_colors = 30
painter = Turtle()
painter.shape("classic")
turtle.colormode(255)

color_list = color_tuple_extraction('image.jpg', num_colors)
final_color_list = color_list[4:] # remove background, list is order by frequency so probably first colors are
# background colors e.g. white

painter.hideturtle()
painter.penup()
start_position_x = - 250.0
start_position_y = - 230.0
painter.setx(start_position_x)
painter.sety(start_position_y)
painter.speed("fastest")

for _ in range(10):
    paint_row_of_dots()
    go_up_one_level(start_position_x, start_position_y)

screen = Screen()
screen.exitonclick()