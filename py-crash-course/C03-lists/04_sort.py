#####      Python Crash Course 09/01/2022  	     #####

# Sorting lists permanently

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()													# Sort list alphabetically and change it permanently
print(cars)

cars.sort(reverse=True)										# revere=True sorts in reverse alphabetical order
print(cars)

# Sorting list temporarily

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("\nHere's the original list:")
print(cars)

print("\nHere's the temporary sorted list:")
print(sorted(cars))											# Temporary sorted list (ASC)

print("\nHere's the original list again:")
print(cars)									

print("\nHere's the reverse alphabetical order list:")
print(sorted(cars, reverse=True))							# Temporary sorted list (DESC)

# Reverse order of list permanently

cars.reverse() 												# Reverse order of list	
print(f"Reverse list: {cars}")

# Finding the lenght of a list

print(len(cars))											# Count num of itens from list and print it
