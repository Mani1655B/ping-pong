from turtle import Turtle, Screen

x = 350


class Paddle:
    def __init__(self):
        self.create_paddle()

    def create_paddle(self):
        self.paddle = Turtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(5, 1)
        self.paddle.penup()
        self.paddle.goto(350, 0)

    def go_up(self):
        if self.paddle.ycor() <= 250:
            y = self.paddle.ycor() + 20
            self.paddle.goto(x, y)

    def go_down(self):
        if -250 <= self.paddle.ycor():
            y = self.paddle.ycor() - 20
            self.paddle.goto(x, y)
