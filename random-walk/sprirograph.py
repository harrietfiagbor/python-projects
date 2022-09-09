import turtle
from turtle import Turtle, Screen
import random

elsa = Turtle()
elsa.speed("fastest")
turtle.colormode(255)


def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_spirograph(size_of_gap):
    for circle in range(int(360 / size_of_gap)):
        elsa.color(change_color())
        elsa.circle(100)
        elsa.left(size_of_gap)


draw_spirograph(7)

screen = Screen()
screen.exitonclick()
