prompt = "What's your age? (Type quit to exit) "

# Using a conditional test
# age = 1
#
# while age > 0:
#     age = input(prompt)
#     if int(age) > 12:
#         price = "$ 15"
#     elif int(age) > 3:
#         price = "$ 10"
#     elif int(age) < 3:
#         price = "free"
#     if int(age) != 0:
#         ticket_msg = f"Your ticket is {price}"
#         print(ticket_msg)

# Using a flag
active = True

while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    else:
        if int(age) > 12:
            price = "$ 15"
        elif int(age) >= 3:
            price = "$ 10"
        elif int(age) < 3:
            price = "free"

        ticket_msg = f"Your ticket is {price}"
        print(ticket_msg)