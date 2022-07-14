numbers = []
i = 5

while i > 0:
    numbers.append(int(input()))
    i -= 1

for n in numbers:
    if n % 2 == 0:
        i += 1

print(f"{i} valores pares")
