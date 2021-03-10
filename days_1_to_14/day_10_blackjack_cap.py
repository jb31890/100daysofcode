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

def win():
    print("You win!")
    bank += bet_amt * 2
    play_again()

def lose():
    print("You lose!")
    play_again()
    
def draw():
    print("Draw!")
    bank +=  bet_amt
    play_again()
    
def play_again():
    again = input("Do you want to play again? y/n ")
    if again.lower() == "y":
        print(bank)
        blackjack(bank)
    elif again.lower() == "n":
        game_over()
    else:
        print("Please enter either 'y' or 'n'")
        play_again()

def game_over():
    print("Thank you for playing!")
    sys.exit(1)
    
def insurance(hand):
    insurance_bet = input("The dealer is showing an Ace, would you like insurance? y/n ")
    if insurance_bet[0].lower() == "y":
        bank -= bet_amt
        if sum(hand) == 21:
            print("Dealer had blackjack, good job on the insurance bet!")
            bank += bet_amt * 2
        else:
            print("Dealer does not have blackjack, good job on the insurance bet!")
    elif insurance_bet[0].lower() == "n" and sum(hand) == 21:
        print("Dealer has blackjack!")
        lose()
    elif insurance_bet[0].lower() == "n" and sum(hand) != 21:
        return
    else:
        print("Please enter y or n")
        insurance(hand)

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
            if 11 not in hit_hand:
                print(f"You busted with {hit_hand}!")
                play_again()
            else:
                hit_hand[hit_hand.index(11)] = 1
                player_choose(hit_hand)
        else:
            player_choose(hit_hand)
    elif choice_ == "stay" or choice_ == "s":
        print(hand)
        return
    elif choice_ == "double-down" or choice_ == "dd":
        bank -= bet_amt
        bet_amt *= 2
        hit(hand)
        if sum(hand) > 21:
            if 11 not in hand:
                print(f"You busted with {hand}!")
                play_again()
            else:
                hand[hand.index(11)] = 1
        else:
            print(f"Your hand is {hand}")
            return hand
    else:
        print("Please enter either hit or stay")
        player_choose(hand)

def dealer_choose(hand):
        if sum(hand) < 17:
            hit_hand = hit(hand)
            if sum(hit_hand) > 21:
                if 11 not in hit_hand:
                  print(f"The dealer has busted with {hit_hand}!")
                  win()
                else:
                    hit_hand[hit_hand.index(11)] = 1
                    dealer_choose(hit_hand)
            else:
                dealer_choose(hit_hand)
        elif sum(hand) >= 17:
            print(f"dealer hand is {hand}")

def blackjack(bank):
    while bank > 0:
        bet_amt = 0
        print(f"You have {bank} in your bank.")
        bet_amt_input = input("Please enter the amount you would like to wager: ")
        try:
            if int(bet_amt_input) in range(bank):
                bet_amt = int(bet_amt_input)
                bank -= bet_amt
            else:
                print(f"Please enter a valid number between 0 and {bank}")
                blackjack(bank)
        except ValueError:
            print(f"Please enter a valid number between 0 and {bank}")
            blackjack(bank)
        player_hand = deal()
        dealer_hand = deal()
        print(f"Your hand: {player_hand}. Dealer hand: [{dealer_hand[0]},*]")
        if sum(player_hand) == 21 and sum(dealer_hand) == 21:
            print("Push, you and the dealer had blackjack!")
            draw()
        elif sum(player_hand) == 21 and sum(dealer_hand) != 21:
            print("Winner! You have blackjack!")
            win()
        elif dealer_hand[0] == 11:
            insurance(dealer_hand)
        elif sum(dealer_hand) == 21:
            print("Dealer has blackjack!")
            lose()
        player_choose(player_hand)
        dealer_choose(dealer_hand)
        if sum(player_hand) > sum(dealer_hand):
            win()
        elif sum(player_hand) < sum(dealer_hand):
            lose()
        else:
            draw()
    print("You are out of money, better luck next time!")

blackjack(bank)