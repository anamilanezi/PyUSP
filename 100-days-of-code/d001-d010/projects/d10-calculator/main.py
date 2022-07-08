import art
import os
from calculations import *

def ask_operator():
    operator = ""
    while operator not in operations:
        operator = input("Pick an operation: ")
        if operator not in operations:
            print("Ups, that's not a valid operator. Try again.")
    return operator

def ask_next_number():
    return float(input("What's the next number? "))

def get_result(n1, op, n2):
    operation = operations[op]
    result = operation(n1, n2)
    text_result = f"{n1} {op} {n2} = {result}"

    print("{:-^33}".format("-"))     # Text decoration
    print(f"|{text_result:^31}|")
    print("{:-^33}".format("-"))     # Text decoration

    return result

def ask_if_continue_with(result):
    use_result = ""
    while (use_result != 'y') or (use_result != 'n'):

        prompt = f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: "
        use_result = input(prompt).lower()

        if use_result == 'y':
            print("")
            return True
        elif use_result == 'n':
            return False
        else:
            print("That's not a valid answer, try again.")

def calculator():

    continue_with_result = True         
    num1 = ask_first_number()
    print_symbols()

    while continue_with_result:
        operator = ask_operator()
        num2 = ask_next_number()    
        result = get_result(num1, operator, num2)

        continue_with_result = ask_if_continue_with(result)

        if continue_with_result:
            num1 = result
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            calculator()

print(art.logo)
calculator()
