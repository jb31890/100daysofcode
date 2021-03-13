# day 15 coffee machine
# 3 types of coffee

import sys
from copy import deepcopy

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

STARTING_RESOURCES = {
    "water": 2000,
    "milk": 2000,
    "coffee": 300,
    "money": 0,
}

COINS = {
    "quarters": .25,
    "dimes": .10,
    "nickles": .05,
    "pennies": .01,
}

def request():
    drinks = [i for i in MENU]
    drink = input(f"What would you like? {drinks}: ")
    if drink.lower() == "off":
        print("Goodbye.")
        sys.exit()
    elif drink.lower() == "report":
        return drink
    elif drink not in drinks:
        print("Error: Please enter a valid menu item.")
        return request()
    return drink

def report(resources):
    print(f"Current inventory of resources is: ")
    for item in resources:
        print(f"{item.title()}: {resources[item]}")

def check_inventory(drink, resources):
    recipe = MENU[drink]['ingredients']
    not_enough =[]
    for item in recipe:
        if recipe[item] > resources[item]:
            not_enough.append(item)
    if len(not_enough) > 0:
        print(f"The machine has an insufficient amount of {not_enough}")
        return False
    return True

def make_drink(drink, resources):
    recipe = MENU[drink]['ingredients']
    for item in recipe:
        resources[item] -= recipe[item]
    print(f"Here is your {drink}. Enjoy!\n\n")

def process_payment(drink, resources):
    cost = 0
    total = 0
    payment = {
        "quarters": 0,
        "dimes": 0,
        "nickles": 0,
        "pennies": 0,
    }
    cost = MENU[drink]['cost']
    print(f"Your drink costs: {cost:.2f}")
    print("Please enter payment in the form of coins; quarters(.25), dimes(.10), nickles(.05), and pennies(.01) are accepted")
    for coin in payment:
        try:
            payment[coin] = int(input(f"How many {coin} would you like to enter: "))
            total += COINS[coin] * payment[coin]
            print(total)
        except ValueError as e:
            print(f"\nError: You entered an invalid number.  Please ensure to only enter numbers.\n")
            return process_payment(drink)
    if total >= cost:
        print("Thank you for your purchase.")
        resources["money"] += cost
        change = total - cost
        if change > 0:
            print(f"Here is ${change:.2f} in change")
    else:
        print("\nYou have provided insufficient funds. Refunding money.\n")
        return drink_machine(resources) 
    return True

def drink_machine(resources):
    current_resources = deepcopy(resources)
    while True:
        drink = request()
        if drink == "report":
            report(current_resources)
        elif check_inventory(drink,current_resources):
            if process_payment(drink, current_resources):
                make_drink(drink,current_resources)

drink_machine(STARTING_RESOURCES)