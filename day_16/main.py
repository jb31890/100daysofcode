from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys
    
def request(coffemaker, moneymachine, menu):
    drink = input(f"What would you like to order? {menu.get_items()}: ")
    if drink.lower() == "off":
        print("Goodbye.")
        sys.exit()
    elif drink.lower() == "report":
        coffemaker.report()
        moneymachine.report()
        return request(coffemaker, moneymachine, menu)
    elif drink not in menu.get_items():
        print("Error: Please enter a valid menu item.")
        return request(coffemaker, moneymachine, menu)
    return menu.find_drink(drink)
    
def drink_machine():
    cm = CoffeeMaker()
    mm = MoneyMachine()
    m = Menu()
    while True:    
        drink = request(cm, mm, m)
        if cm.is_resource_sufficient(drink):
            if mm.make_payment(drink.cost):
                cm.make_coffee(drink)

drink_machine()