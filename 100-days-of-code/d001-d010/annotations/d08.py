
# Function that allows for input
def greet(name):
    print("{:=^25}".format(f"Hello, {name}"))
    print("{:=^25}".format("my dear"))
    print("{:=^25}".format("friend"))
    print()

greet("Ana")

# Function with more than 1 input
def greet_with_location(name, location):
    print("{:~^25}".format(f"Good day, {name}"))
    print("{:~^25}".format("how is the weather in"))
    print("{:~^25}".format(f"{location}?"))
    print()

# Positional argument
greet_with_location("Angela", "London")

# Keyword argument
greet_with_location(location="the Moon", name="April")
