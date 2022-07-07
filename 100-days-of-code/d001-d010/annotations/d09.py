programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

# Dictionaries have elements which are identified by their key:
# print(programming_dictionary["Bug"])

# Data types should be valid and accordingly with the key:value pair used in the dictionary construction
bug = "Bug"
programming_dictionary = {
    bug: "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
	123: "An integer",
}

# print(programming_dictionary[bug])
# print(programming_dictionary[123])

# Adding new items to dictionary:
programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

# Create an empty dictionary:
empty_dictionary = {}

# Wipe an existing dictionary:
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary:
programming_dictionary["Bug"] = "A moth in your computer."

# Loop through a dictionary:

# The default syntax uses de key as the arbitrary variable and than we can access the values :
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# This syntax gives the key:value pair:
for item in programming_dictionary.items():
    print(item)
# ('Bug', 'A moth in your computer.')
# ('Function', 'A piece of code that you can easily call over and over again.')
# (123, 'An integer')
# ('Loop', 'The action of doing something over and over again.')

# This syntax gives only the values without it corresponding key
for value in programming_dictionary.values():
    print(value)

################################################################

# Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Humburg", "Stuttgart"],
}

# Nesting dictionary in a dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Humburg", "Stuttgart"],
        "total_visits": 5,
    },
}

# Nesting a dictionary in a list
travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Humburg", "Stuttgart"], "total_visits": 5
    },
]

print(travel_log[0]["country"])