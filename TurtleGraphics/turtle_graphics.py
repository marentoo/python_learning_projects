import turtle
from turtle import Turtle, Screen, colormode
import random
import time

tim = Turtle()
tim.shape("turtle")
turtle.colormode(255)
# turtle_colors = ["red", "blue", "green", "yellow", "purple", "orange", "brown", "pink", "cyan", "magenta"]
# tim_color = lambda: tim.color(random.choice(turtle_colors), random.choice(turtle_colors))

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple

#Exercise 1 Draw triangle, square, pentagon...
def draw_shape(number_of_sides):
    tim.color(random_color())
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        tim.forward(100)
        tim.right(angle)


# for i in range(3, 11):
#     draw_shape(i)
#     i += 1
# screen = Screen()
# screen.exitonclick()




#Exercise 2 Random Walk - thickness, color, speed up
directions = [0, 90, 180, 270]
movement = [0, 30]
thickness = [10]
speed = ["slow", "fastest"]

def random_movement():
    tim.forward(random.choice(movement))
    return tim.setheading(random.choice(directions))

# start_time = time.time()
# while (time.time() - start_time) < 100:
#     random_movement()
#     tim.color(random_color())
#     tim.pensize(random.choice(thickness))
#     tim.speed(random.choice(speed))




#Exercise 3 - Spirograph
def draw_spirograph(size):
    number_of_circles = int(360/size)
    for _ in range(number_of_circles):
        tim.color(random_color())
        tim.speed("fastest")
        tim.circle(radius = 100)
        tim.setheading(tim.heading() + size)


draw_spirograph(5)
screen = turtle.Screen()
screen.exitonclick()