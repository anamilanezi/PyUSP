# RANDOMISATION

# import random

# # Random integer between 1 and 10 (included)
# random_integer = random.randint(1,10)
# print(random_integer)

# # Random floating number between 0.0 and 1.0 (1.0 excluded)
# random_float = random.random() * 10
# print(random_float)

# Nested lists

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)


print(dirty_dozen[0])
print(dirty_dozen[1])

print(dirty_dozen[1][2])
print(dirty_dozen[1][3])
print(dirty_dozen[1][1])

row1 = ["00","01","02"]
row2 = ["10","11","12"]
row3 = ["20","21","22"]
map = [row1, row2, row3]
print(map[0][2])