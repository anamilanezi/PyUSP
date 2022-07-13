from menu import *

take_order = True

# TODO 1. Asks which drink the user wants

# order = input("What would you like? (espresso/latte/cappuccino): ")
# drink = MENU[order]
# drink_cost = drink['cost']

# TODO: 2. Print a report of all coffee machine resources when user types 'report'


def process_report(resources_data):

    for resource in resources_data:
        if resource == 'money':
            print(f"{resource.title()}: ${resources_data[resource]}")
        elif resource == 'coffee':
            print(f"{resource.title()}: {resources_data[resource]}g")
        else:
            print(f"{resource.title()}: {resources_data[resource]}ml")

# TODO: 3. Checks if there is enough resources to make the drink


def process_drink(drink_order, resources_data):

    ingredients = drink_order['ingredients']

    for ingredient in ingredients:
        if ingredient in resources_data:
            if (resources_data[ingredient] - ingredients[ingredient]) >= 0:
                resources_data[ingredient] -= ingredients[ingredient]
            else:
                print(f"Sorry there is not enough {ingredient}.")
                return False
    return True

# TODO: 4. Asks for the coins to be inserted


def insert_coins(coins_data):
    total_dollars = []
    for coin in coins_data:
        insert = int(input(f"How many {coin}?: "))
        total_inserted = insert * coins_data[coin]
        total_dollars.append(total_inserted)

    return sum(total_dollars)


# TODO: 5. Checks if there is enough money to pay for the drink
# TODO: 6. Calculate the change

def check_payment(total_inserted, cost):

    change = total_inserted - cost
    if change >= 0:
        print(f"Here is ${round(change,2)} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def take_order():

    order = input("What would you like? (espresso/latte/cappuccino): ")

    if order == 'report':
        process_report(resources)
        take_order()
    elif order == 'quit':
        quit()
    else:
        drink = MENU[order]
        drink_cost = drink['cost']
        available_resources = process_drink(drink, resources)

        if available_resources:

            print("Please insert coins.")
            total = insert_coins(coins)

            if check_payment(total, drink_cost):
                resources['money'] += drink_cost

            print(f"Here is your {order} ☕. Enjoy! ")
            take_order()
        else:
            take_order()


take_order()






