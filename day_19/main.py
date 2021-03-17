from turtle import Turtle, Screen
from random import randint
from sys import exit
from time import sleep

screen =  Screen()
screen.colormode(255)
screen.setup(width=600, height=400)

RACERS = ["deebo", "taytay", "gary", "kegs", "jon"]

def random_color(turtle):
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    turtle.color(r, g, b)

def win_or_lose(turtle, user, winner):
    if user == winner:
        screen.clear()
        turtle.reset()
        turtle.write("You Won!", True, align="left", font=("Arial", 10, "normal"))
        play_again()
    else:
        screen.clear()
        turtle.reset()
        turtle.write("You Lost!", True, align="left", font=("Arial", 10, "normal"))
        play_again()

def play_again():
    user_choice = screen.textinput(title="Play Again?", prompt="Would you like to play again? ")
    if user_choice[0].lower == "y":
        return race()
    else:
        print("Goodbye.")
        sys.exit()

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
                sleep(1)
                win_or_lose(racer, user_choice, winner)

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