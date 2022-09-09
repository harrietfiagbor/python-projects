from turtle import Turtle


class Divider(Turtle):

    def __init__(self):
        super().__init__("square")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setheading(90)
        self.x_axis = 0
        self.y_axis = -300
        self.setposition(self.x_axis, self.y_axis)
        self.width(10)
        self.draw_dashed_line()
        # self.shapesize(stretch_wid=1, stretch_len=0.5)

    def draw_dashed_line(self):
        for i in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
            self.y_axis += 10
