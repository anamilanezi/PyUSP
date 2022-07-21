poll_responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat's your name? ")
    response = input("If you could visit one place in the world, where would you go? ")

    poll_responses[name] = response
    continue_poll = input("Would you like to let another person respond? (yes/no) ")
    if continue_poll.lower() == 'no':
        polling_active = False

print(f"{'Dream Vacation Results':-^50}")
for name, response in poll_responses.items():
    print(f"{name.title()} wants to go to {response.title()}")