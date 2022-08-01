x = int(input())
z = int(input())
soma = []

while x >= z:
    z = int(input())

for n in range(x, z):
    soma.append(n)
    if sum(soma) > z:
        print(len(soma))
        break

