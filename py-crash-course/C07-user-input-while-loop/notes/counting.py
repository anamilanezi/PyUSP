# Using continue to return to the beginning of the loop based on the result of a conditional test

current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:   # If the number is even, won't reach the print line
        continue
    print(current_number)