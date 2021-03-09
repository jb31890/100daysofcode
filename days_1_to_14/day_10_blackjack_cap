# day 10 capstone blackjack game

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

from random import choice
import sys

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
bank = 100

def deal():
    hand = []
    for card in range(2):
        hand.append(choice(cards))
    return hand
    
def hit(hand):
    hand.append(choice(cards))
    return hand

def double_down(hand):
    return hand

def win():
    print("You win!")
    play_again()
    
def play_again():
    again = input("Do you want to play again? y/n ")
    if again.lower() == "y":
        blackjack()
    elif again.lower() == "n":
        game_over()
    else:
        print("Please enter either 'y' or 'n'")
        play_again()

def game_over():
    print("Thank you for playing!")
    sys.exit(1)
    
def insurance():
    return

def bet():
    return

def player_choose(hand):
    choice_ = ""
    if len(hand) == 2:
        choice_ = input("Would you like to hit(h), double-down(dd), or stay(s)? ")
    else:
        print(hand)
        choice_ = input("Would you like to hit or stay? ")

    if choice_ == "hit" or choice_ == "h":
        hit_hand = hit(hand)
        if sum(hit_hand) > 21:
            print(f"You busted with {hit_hand}!")
            play_again()
        else:
            player_choose(hit_hand)
    elif choice_ == "stay" or choice_ == "s":
        print(hand)
        return hand
    elif choice_ == "double-down" or choice_ == "dd":
        double_down(hand)
    else:
        print("Please enter either hit or stay")
        player_choose(hand)

def dealer_choose(hand):
        if sum(hand) < 17:
            hit_hand = hit(hand)
            if sum(hit_hand) > 21:
                print(f"The dealer has busted with {hit_hand}!")
                win()
            else:
                dealer_choose(hit_hand)
        elif sum(hand) >= 17:
            print(f"dealer hand is {hand}")
            return hand


def blackjack():
    bet()
    player_hand = deal()
    dealer_hand = deal()
    print(f"Your hand: {player_hand}. Dealer hand: [{dealer_hand[0]},*]")
    if sum(player_hand) == 21:
        print("Blackjack!")
        win()
    if dealer_hand[0] == 11:
        insurance()
    player_choose(player_hand)
    #dealer_hand = dealer_choose(dealer_hand)
    dealer_choose(dealer_hand)
    #print(player_hand)
    #print(dealer_hand)
    if sum(player_hand) > sum(dealer_hand):
        win()
    elif sum(player_hand) < sum(dealer_hand):
        print("You lose!")
        play_again()
    else:
        draw()

blackjack()
    
    
