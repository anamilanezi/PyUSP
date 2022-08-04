# X=4 Y=3 > 5 + 7 + 8

nt = int(input())

for _ in range(nt):
    teste = input().split()
    X = int(teste[0])
    Y = int(teste[1])
    soma = []
    while len(soma) < Y:
        if X % 2 != 0:
            soma.append(X)
        X += 1
    print(sum(soma))


