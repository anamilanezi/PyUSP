numbers = []
i = 6

while i > 0:
    numbers.append(float(input()))
    i -= 1


for n in numbers:
    if n <= 0:
        numbers.remove(n)

i = len(numbers)
media = round(sum(numbers)/i, 2)

print(f"{i} valores positivos")
print(f"{media}")