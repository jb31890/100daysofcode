#day 12

# guessing game final

from random import choice
import sys

def play_again():
    again = input("Do you want to play again? y/n ")
    if again.lower() == "y":
        guessing_game()
    elif again.lower() == "n":
        print("Goodbye.")
        sys.exit(1)
    else:
        print("Please enter either 'y' or 'n'")
        play_again()

def pick_number():
    print("I'm thinking of a number between 1 and 100.")
    picked_number = choice(range(1,101))
    return picked_number

def pick_difficulty():
    valid_inputs = ["easy", "hard"]
    picked_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if picked_difficulty.lower() in valid_inputs:
        if picked_difficulty.lower() == "easy":
            return 10
        else:
            return 5 
    else:
        print("Please enter a valid answer")
        return pick_difficulty()

def guess(chosen_number, number_of_guesses):
    while number_of_guesses > 0:
        print(f"You have {number_of_guesses} remaining to guess the number.")
        current_guess = input("Make a guess: ")
        try:
            int(current_guess) in range(1,101)
            current_guess = int(current_guess)
            if current_guess == chosen_number:
                print(f"You got it! The answer was {chosen_number}")
                return play_again()
            elif current_guess > chosen_number:
                print("Too high.\nGuess again.")
                return guess(chosen_number, number_of_guesses-1)
            else:
                print("Too low.\nGuess again.")
                return guess(chosen_number, number_of_guesses-1)
        except ValueError:
            print("Please enter a valid answer")
    print("You've run out of guesses, you lose.")

def guessing_game():
    print("Hello and welcome to the Guessing Game!")
    number = pick_number()
    guesses = pick_difficulty()
    guess(number, guesses)
    print(f"the number was {number}")
    play_again()

guessing_game()