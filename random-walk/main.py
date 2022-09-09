import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("aquamarine")
screen = Screen()
turtle.colormode(255)


def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


coords = [0, 90, 180, 270]
colors = ["peru", "light gray", "violet", "coral", "crimson", "rosy brown",
          "deep pink", "indigo", "salmon", "red", "blue"]
tim.speed("fastest")


def move_random(steps):
    tim.pensize(10)
    # tim.penup()
    # tim.setpos(-180, -180)
    # tim.pendown()
    for _ in range(steps):
        tim.forward(50)
        tim.seth(random.choice(coords))
        tim.color(change_color())
        # tim.color(random.choice(colors))


move_random(50000)

screen.exitonclick()
