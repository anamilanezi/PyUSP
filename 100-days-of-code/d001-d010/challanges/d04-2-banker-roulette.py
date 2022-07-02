import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

#Write your code below this line 👇
random_name = names[random.randint(0, len(names)-1)]

# random_name = random.choice(names) will pick a random item from the list

print(f"{random_name} is going to buy the meal today!")
