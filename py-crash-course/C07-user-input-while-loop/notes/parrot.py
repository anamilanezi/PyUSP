prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# Using a flag to control the loop flow
active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
