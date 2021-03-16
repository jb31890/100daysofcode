from turtle import Turtle, Screen
from random import randint

screen =  Screen()
screen.colormode(255)
screen.setup(width=600, height=400)

RACERS = ["deebo", "taytay", "gary", "kegs", "jon"]

def random_color(turtle):
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    turtle.color(r, g, b)

def race():
    winner = ""
    racers = make_racers()
    move_to_starting_line(racers)
    user_choice = screen.textinput(title="Select your winner", prompt="Who do you think will win the race?: ")
    while winner == "":
        for racer in racers:
            racer.forward(randint(1,5))
            if racer.xcor() >= 200:
                winner = RACERS[racers.index(racer)]
                racer.write("WINNER!", True, align="left", font=("Arial", 10, "normal"))
    if user_choice == winner:
        print("You won!")
    else:
        print("you lose!")

def make_racers():
    racers = []
    for racer in RACERS:
        racer = Turtle(shape="turtle")
        random_color(racer)
        racers.append(racer)
        racer.pu()
    return racers

def move_to_starting_line(list_of_racers):
    start = ((screen.window_height() / 2) * -1) + 100
    for racer in list_of_racers:
        racer.goto(x=-240, y=start)
        racer.write(RACERS[list_of_racers.index(racer)], True, align="left", font=("Arial", 10, "normal"))
        racer.goto(x=-180, y=start)
        start += 50

race()

screen.exitonclick()