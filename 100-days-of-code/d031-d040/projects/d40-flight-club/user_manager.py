import data_manager

print("Welcome to the Flight Club.\nWe find the best flight deals and email you")

name = input("What is your first name?\n")
last = input("What is your last name?\n")

valid_email = False

while not valid_email:
    email1 = input("What is your email?\n")
    email2 = input("Type your email again.\n")
    valid_email = (email1 == email2)
    if valid_email:
        print("Welcome to the flight club!")
        data = data_manager.DataManager()
        data.new_user(name, last, email1)
    else:
        print("Your email don't match, please try again.")
