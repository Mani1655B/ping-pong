from turtle import Turtle

x_change = -10
y_change = -10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        self.goto(self.xcor() + x_change, self.ycor() + y_change)

    def v_bounce(self):
        global y_change
        y_change *= -1

    def h_bounce(self):
        global x_change
        x_change *= -1
