from turtle import Turtle
from random import randint
from random import choice
from time import sleep

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():

    def __init__(self):
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE
        self.controller()
        #self.create_cars()
        
    def create_cars(self):
        car = Turtle(shape="square")
        car.shapesize(1, 2, .1)
        car.pu()
        car.speed("fastest")
        car.color(choice(COLORS))
        car.goto(randint(-280,300),randint(-250,260))
        car.seth(180)
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.move_speed)
            if car.xcor() < -320:
                car.goto(randint(300,400),randint(-250,260))

    def controller(self):
        for _ in range(25):
            self.create_cars()

    def increase_level(self):
        self.move_speed += MOVE_INCREMENT

