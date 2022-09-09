import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
turtle.hideturtle()
user_bet = turtle.textinput(title="Make your bet", prompt="Which turtle will win: type the color")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
all_turtles = []

x_cord = -230
y_cord = -150

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x_cord, y_cord)
    all_turtles.append(new_turtle)
    y_cord += 50

end_game = True

if user_bet:
    end_game = False


while not end_game:
    for turtle in all_turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)
        if turtle.xcor() > 230:
            end_game = True
            winning_turtle = turtle.pencolor()
            if user_bet == winning_turtle:
                print(f"You've won! The {winning_turtle} turtle is the winner")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner")


screen.exitonclick()
