from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
take_order = True

while take_order:
    order = input(f"What would you like? ({menu.get_items()}): ")

    if order == 'report':
        coffee_maker.report()
        money_machine.report()
    elif order == 'off':
        take_order = False
    else:
        drink = menu.find_drink(order)
        if not drink:
            print("Please, try again.")
        else:
            cost = drink.cost
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(cost):
                coffee_maker.make_coffee(drink)

