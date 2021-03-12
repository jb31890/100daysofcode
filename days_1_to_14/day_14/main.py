from art import logo, vs
from data import data
from random import choice
import sys

#while true print logo \n choice 1 \n vs \n choice 2
# if correct, make previous correct choice choice1 and vs new choice 2

def option():
    o = choice(data)
    return o

def against():
    choice(data)

def choose(a,b):
    correct = False
    allowed_inputs = ["A", "B"]
    a_or_b = input("Who has more followers? Type 'A' or 'B': ")
    if a_or_b not in allowed_inputs:
        print("Please enter either 'A' or 'B'")
        return choose(a,b)
    if a['follower_count'] > b['follower_count']:
        if a_or_b == "A":
            correct = True
            return correct, a
    elif b['follower_count'] > a['follower_count']:
        if a_or_b == "B":
            correct = True
            return correct, b
    else:
        return correct 

def game():
    score = 0
    a = {}
    b = {}
    while True:
        print(logo)
        if score > 0:
            print(f"you right, you're score is {score}")
        if a =={}:
            a = option()
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
        print(vs)
        b = option()
        #if a == b then regen b until not the same
        while a == b:
            b = option()
        print(f"Compare A: {b['name']}, a {b['description']}, from {b['country']}")
        c = choose(a,b)
        if c:
            score += 1
            a = c[1]
            b = {}
        else:
            print(f"You lose, your score was {score}")
            sys.exit(1)
        
game()