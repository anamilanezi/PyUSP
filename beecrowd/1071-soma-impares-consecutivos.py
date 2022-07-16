x = int(input())
y = int(input())
numeros = []

for n in range(y + 1, x):
    if n % 2 != 0:
        numeros.append(n)

print(sum(numeros))