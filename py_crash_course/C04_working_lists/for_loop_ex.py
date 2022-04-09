# 4.3 Use a for loop to print the numbers from 1 to 20, inclusive:

numbers = list(range(1,21))
for number in numbers:
    print(number)

for number in range(1,21):
    print(number)

# 4.4 Make a list of the numbers from one to one million, and then use a for loop to print the numbers.

million = list(range(1,1000001))
for value in million:
    print(value)

# 4.5 

max(million)
min(million)
sum(million)

# 4.6

even_numbers = list(range(1,21,2))

# 4.7 Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list

threes = list(range(3,31,3))
for number in threes:
    print(number)

threes = []
for number in range(1,11):
    new_number = number * 3
    threes.append(new_number)
    print(new_number)

threes = []
for number in range(1,11):
    threes.append(number*3)

threes = [number*3 for number in range(1,11)]

# 4.8 Make a list of the first 10 cubes

cubes = []
for value in range(1,11):
    cube = value ** 3
    cubes.append(cube)
    print(cube)

for value in range(1,11):
    cubes.append(value**3)
print(cubes)

# 4.9

cubes = [value**3 for value in range(1,11)]
print(cubes)

