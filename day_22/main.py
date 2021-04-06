#!/usr/bin/env python

# this is the main file for day 22
# we are building a pong game


from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG!")
screen.tracer(0)

sb = Scoreboard()
r_paddle = Paddle(starting_pos=(350, 0))
l_paddle = Paddle(starting_pos=(-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_running = True
while game_is_running:
    screen.update()
    time.sleep(ball.move_speed)

    ball.move()

    if ball.ycor() >= 290 or ball.ycor() <= -275:
        ball.y_bounce()

    if ball.distance(r_paddle) < 55 and ball.xcor() > 320 or ball.distance(l_paddle) < 55 and ball.xcor() < -320:
        ball.x_bounce()

    if ball.xcor() >= 380:
        sb.left += 1
        sb.increase_score()
        ball.reset("left")
    elif ball.xcor() <= -380:
        sb.right += 1
        sb.increase_score()
        ball.reset("right")

screen.exitonclick()
