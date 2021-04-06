from turtle import Turtle
from random import randint
import time

BALL_SPEED = 10

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = BALL_SPEED
        self.y_move = BALL_SPEED
        self.move_speed = 0.1
        
    def create_ball(self):
        self.shape("circle")
        self.pu()
        self.speed("fast")
        self.color("white")

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= .9

    def reset(self, direction):
        if direction == "left":
            self.x_move = -BALL_SPEED
        else:
            self.x_move = BALL_SPEED

        self.goto(0,0)
        self.move_speed = 0.1
        time.sleep(0.2)
