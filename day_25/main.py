#!/usr/bin/env python

import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. Game")

img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
#print(data.state)
score = 0
answers = []

def guess():
    guess = screen.textinput(f"{score}/50 States Correct", "What is your guess?: ").title()
    print(guess)
    if guess in data.state.tolist():
        writer = turtle.Turtle()
        writer.pu()
        writer.ht()
        writer.goto(data[data.state == guess].x.item(),data[data.state == guess].y.item())
        writer.write(guess, align="Left")
        #print(data[data.state == guess].x.to_string(index=False))
        #print(data[data.state])
        answers.append(guess)
    else:
        game_over()
        print("booo")

def game_over():
    pass


game_is_running = True
while game_is_running:
    
    guess()

screen.exitonclick()
