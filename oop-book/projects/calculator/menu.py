from calculator import Calculator
from prettytable import PrettyTable


import sys

class Menu:

    def __init__(self):
        self.calculator = Calculator()
        self.operations = {
            "+": self.calculator.add,
            "-": self.calculator.subtract,
            "x": self.calculator.multiply,
            "/": self.calculator.divide,
            "sqr": self.calculator.square_root,
            "mod": self.calculator.modulus,
        }
        self.options = {
            "memory": self.memory,
            "quit": self.quit,
        }

    def display_menu(self):
        print(
            """
            Pycalc 1.0
            --------------------
            |  +  |  -  | √sqr |  
            --------------------
            |  x  |  /  | mod  | 
            --------------------  
            |   Memory  | quit |
            --------------------
            """
        )

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option: ").lower()
            operation = self.operations.get(choice)
            option = self.options.get(choice)
            if operation:
                result = operation()
                # self.calculator.memory.append(result)
                print(result)
            elif option:
                option()
            else:
                print("Invalid input")

    def memory(self):
        table = PrettyTable()
        table.add_column("Calculus", self.calculator.calc_memory)
        table.add_column("Results", self.calculator.result_memory)
        print(table)


    def quit(self):
        print("Thank you for using the calculator")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
