#!/usr/bin/env python

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
screen.update()
time.sleep(.5)
player = Player()
sb = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move()
    screen.update()

    if player.ycor() >= 290:
        sb.increase_level()
        player.reset()
        car_manager.increase_level()

    for car in car_manager.cars:
        if player.distance(car) <= 20:
            game_is_on = False
            sb.game_over()


screen.exitonclick()
