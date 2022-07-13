import random

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

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
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

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# position = 0
# for char in password_list:
#     password += password_list[position]
#     position += 1
#     print(password)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


# Using lists methods with random numbers
final_range = len(password_list)    # Final range is not included, last position on list = (final_range - 1)

for char in range(0,final_range):
    # randint includes both  
    random_position = random.randint(0,len(password_list) - 1)
    random_char = password_list[random_position]
    password += random_char
    password_list.remove(random_char)
print(f"Here is your password: {password}")

# Using random.shuffle:

# random.shuffle(password_list) 

# for char in password_list:
#     password += char
# print(f"Here is your password: {password}")
