from turtle import Turtle

# CONSTANTS
WIDTH = 1
HEIGHT = 5
MOVE_DISTANCE = 20
ANGLE = 90
RIGHT_COORD = (350, 0)
LEFT_COORD = (-350, 0)


class Paddle(Turtle):

    def __init__(self,  position):
        super().__init__("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=HEIGHT, stretch_len=WIDTH)
        self.setposition(position)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
