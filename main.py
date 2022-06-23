from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_on = True
machine = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

choice = input("What would you like? (espresso/latte/cappuccino/):").lower()

if choice == "off":
    is_on = False
elif choice == 'report':
    print(f"{machine.report()}\n {money.report()}")
else:
    drink = menu.find_drink(choice)
    order = machine.is_resource_sufficient(drink)
    cost = drink.cost
    payment = money.make_payment(cost)
    make = machine.make_coffee(drink)
    
    