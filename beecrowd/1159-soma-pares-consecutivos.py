x = int(input())

while x != 0:
    soma = []
    while len(soma) < 5:
        if x % 2 == 0:
            soma.append(x)
        x += 1
    print(sum(soma))
    x = int(input())

