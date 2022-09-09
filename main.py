import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball, ball_speed
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((365, 0))
l_paddle = Paddle((-365, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()

    # collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.paddle_bounce()
        ball.inc_speed()

    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()
        ball.move_speed = ball_speed

    if ball.xcor() < -395:
        ball.reset_position()
        scoreboard.r_point()
        ball.move_speed = ball_speed
screen.exitonclick()
