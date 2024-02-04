from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.title("PING PONG")
screen.bgcolor("black")
screen.setup(800, 600)
paddle = Paddle()
ball = Ball()

screen.listen()
screen.onkeypress(paddle.go_up, "Up")
screen.onkeypress(paddle.go_down, "Down")
game_is = True
while game_is:
    ball.move()
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.v_bounce()  # bounce vertically
    elif ball.xcor() <= -390:
        ball.h_bounce()  # bounce horizontally
    elif ball.xcor() >= paddle.paddle.xcor()-20 and paddle.paddle.ycor() - 50 <= ball.ycor() <= paddle.paddle.ycor() + 50:
        ball.h_bounce()
    elif ball.xcor()>=390:
        paddle.paddle.hideturtle()
        paddle.paddle.home()
        paddle.paddle.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
        game_is=False


screen.exitonclick()
