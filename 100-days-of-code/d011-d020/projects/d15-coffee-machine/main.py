from menu import *
import os


def clear():
    """'Clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def process_report():
    """Prints the current availability of ingredients and money on machine."""
    for resource in resources:
        if resource == 'money':
            print(f"{resource.title()}: ${resources[resource]}")
        elif resource == 'coffee':
            print(f"{resource.title()}: {resources[resource]}g")
        else:
            print(f"{resource.title()}: {resources[resource]}ml")


def check_resources(drink_type):
    """Returns true if there is enough ingredients for ordered drink, false if not."""
    ingredients = drink_type['ingredients']

    for ingredient in ingredients:
        if ingredient in resources:
            if resources[ingredient] >= ingredients[ingredient]:
                return True
            else:
                print(f"Sorry there is not enough {ingredient}.")
                return False


def process_coins():
    """Asks for coin of each value and returns the total dollars inserted."""
    total_dollars = []
    for coin in coins:
        inserted_coins = int(input(f"How many {coin}?: "))
        total_inserted = inserted_coins * coins[coin]
        total_dollars.append(total_inserted)

    return sum(total_dollars)


def check_payment(total_inserted, cost):
    """Returns true if the payment is sufficent to pay for the ordered drink, false if not."""
    change = total_inserted - cost
    if change >= 0:
        print(f"Here is ${round(change,2)} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_type):
    """Updates resources availability according to ordered drink"""
    ingredients = drink_type['ingredients']

    for ingredient in ingredients:
        if ingredient in resources:
            resources[ingredient] -= ingredients[ingredient]


def take_order():
    """Takes a coffee order."""
    order = input("What would you like? (espresso/latte/cappuccino): ")

    if order == 'report':
        process_report()

    elif order == 'quit':
        quit()
    else:
        drink = MENU[order]
        drink_cost = drink['cost']
        available_resources = check_resources(drink)

        if available_resources:

            print("Please insert coins.")
            total = process_coins()

            if check_payment(total, drink_cost):
                make_coffee(drink)
                resources['money'] += drink_cost
                print(f"Here is your {order} ☕. Enjoy! ")

    take_order()


take_order()
