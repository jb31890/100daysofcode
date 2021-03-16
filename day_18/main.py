from turtle import Turtle, Screen
from copy import deepcopy
from random import randint, choice
import colorgram

mitch = Turtle()
mitch.shape("turtle")
mitch.color("goldenrod")
screen =  Screen()
screen.colormode(255)
screen.screensize(3000,3000)



def square(turtle, size):
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)

def dashed_square(turtle, size, dash_length):
    on_off = "on"
    for i in range(4):
        current = 0
        while current <= size:
            if on_off == "on" and dash_length <= (size-current):
                turtle.pd()
                turtle.forward(dash_length)
                turtle.pu()
                current += dash_length
                on_off = "off"
            elif on_off == "off" and dash_length <= (size-current):
                turtle.forward(dash_length)
                current += dash_length
                on_off = "on"
            else:
                turtle.forward(1)
                current += 1
        turtle.right(90)

#square(mitch, 100)
#mitch.left(180)
#dashed_square(mitch, 100, 23)

def random_color(turtle):
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    turtle.pencolor(r, g, b)


def shapes(turtle, size, sides):
    for side in range(3,sides):
        random_color(turtle)
        angle = 360/side
        print(side, angle)
        while side > 0:
            turtle.forward(size)
            turtle.right(angle)
            side -= 1

#shapes(mitch, 100, 20)


def random_walk(turtle, distance, screen):
    turtle.width(5)
    turtle.speed(0)
    screen.delay(1)
    for _ in range(distance):
        random_color(turtle)
        turtle.forward(randint(3,69))
        turtle.right(randint(0,359))

#random_walk(mitch, 10000, screen)
#ts = mitch.getscreen()
#ts.getcanvas().postscript(file="random_walk.eps")


def spirograph(turtle):
    turtle.speed(0)
    screen.delay(1)
    for _ in range(1000):
        random_color(turtle)
        turtle.circle(randint(5, 100))
        turtle.right(10)

#spirograph(mitch)

def color_pallette(img):
    return colorgram.extract(img, 10)

def dot_painting(turtle, size):
    turtle.speed(0)
    screen.delay(1)
    turtle.ht()
    colors = color_pallette("day_18\pic.jpg")
    for line in range(size):
        for dot in range(size):
            turtle.pu()
            turtle.dot(20, choice(colors).rgb)
            turtle.forward(50)
        turtle.right(180)
        turtle.forward(50*size)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)

            
dot_painting(mitch, 10)


screen.exitonclick()