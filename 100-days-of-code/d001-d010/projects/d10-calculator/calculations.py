def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def module(n1, n2):
    return n1 % n2

def divide_int(n1, n2):
    return n1 // n2

def ask_first_number():
    return float(input("What's the first number? "))

def print_symbols():
    for symbol in operations:
        print(f"|{symbol:^31}|")

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '%': module,
    '//': divide_int,
}