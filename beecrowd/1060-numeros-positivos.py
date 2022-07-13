numbers = []
i = 6

while i > 0:
    numbers.append(float(input()))
    i -= 1


for n in numbers:
    if n > 0:
        i += 1

print(f"{i} valores positivos")