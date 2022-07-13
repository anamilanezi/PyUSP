import random
import os

logo = """ 
         ___  _   _           _____     ______     
        /   || | | |         |  _  |    |  _  \    
 _ __  / /| / __) __)_      _| |/' |_ __| | | |    
| '_ \/ /_| \__ \__ \ \ /\ / /  /| | '__| | | |    
| |_) \___  (   (   /\ V  V /\ |_/ / |  | |/ /     
| .__/    |_/|_| |_|  \_/\_/  \___/|_|  |___/      
| |                                                
|_|                                                
  ____      _   _  ___________  ___  ______        
 / ___|    | \ | ||____ | ___ \/   ||___  /        
/ /___  ___|  \| |    / / |_/ / /| |   / /__  _ __ 
| ___ \/ _ \ . ` |    \ \    / /_| |  / / _ \| '__|
| \_/ |  __/ |\  |.___/ / |\ \___  |./ / (_) | |   
\_____/\___\_| \_/\____/\_| \_|  |_/\_/ \___/|_|   
"""
def clear():
    ''''Clear the screen'''
    os.system('cls' if os.name == 'nt' else 'clear')

def restart():
    '''Asks the user if wants to play again after finishing a game'''
    user_input = input("Do you want to generate another password? Type 'y' or 'n': "). lower()
    if (user_input.lower() == 'y'):
        return True
    elif (user_input.lower() == 'n'):
        return False

def print_lines():
    '''Prints a line of hifen for decoration'''
    print(f"{'-':-^55}")

def start():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    clear()
    print(logo)
    print("Welcome to the PyPassword Generator!")
    print_lines()
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    password_list = []
    password = ""

    for letter in range(0, nr_letters):
        letter = random.choice(letters)
        password_list.append(letter)

    for symbol in range(0, nr_symbols):
        symbol = random.choice(symbols)
        password_list.append(symbol)

    for number in range(0, nr_numbers):
        number = random.choice(numbers)
        password_list.append(number)

    random.shuffle(password_list) 

    for char in password_list:
        password += char
    
    print_lines()
    print(f"Here is your password: {password}")
    print_lines()

    if restart():
        clear()
        start()
    else:
        print("Thank you for using the Password Generator! :)")
        quit()

start()