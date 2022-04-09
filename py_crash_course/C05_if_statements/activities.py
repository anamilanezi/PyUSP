# 5.5

alien_color = 'green'

if alien_color == 'green':
	print(f"You just earned 5 points.")
elif alien_color == 'yellow':
	print(f"You just earned 10 points.")
elif alien_color == 'red':
	print(f"You just earned 15 points.")

# Versao 2

alien_color = 'red'	

if alien_color == 'green':
	points = 5
elif alien_color == 'yellow':
	points = 10
elif alien_color == 'red':
	points = 15
	
print(f"You earned {points} points!")

# Versao 3

alien_color = 'yellow'	

if alien_color == 'green':
	points = 5
elif alien_color == 'yellow':
	points = 10
elif alien_color == 'red':
	points = 15
	
print(f"You earned {points} points!")

# 5.8

usernames = ['admin','lionel','mafofita','ana','messi']

for username in usernames:
    if username.lower() == 'admin':
        print(f"Hello, {username.title()}, would you like to see a status report?")
    else:
        print(f"Welcome, {username.title()}, thank you for logging in!")
# 5.9

usernames = []

if usernames:    
    for username in usernames:
        if username.lower() == 'admin':
            print(f"Hello, {username.title()}, would you like to see a status report?")
        else:
            print(f"Welcome, {username.title()}, thank you for logging in!")
else:
    print("We need to find some users!")

# 5.10

current_users = ['admin','lionel','mafofita','ana','messi']
new_users = ['luan','ricardo','maria','ana','Lionel']

for user in new_users:
    if user.lower() in current_users:
        print(f"Sorry, this username {user} is already taken. Please, chose a new one.")
    else:
        print(f"Ths username {user} is available.")
        
# 5.11 

ordinal = list(range(1,10))

for value in ordinal:
    if value == 1:
        print(f"{value}st")
    elif value == 2:
        print(f"{value}nd")
    elif value == 3:
        print(f"{value}rd")
    else:
        print(f"{value}th")

# 5.13

# Ideias de programas:
# - Tabela co campeonato brasileiro (série A e B)

