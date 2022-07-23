testes = int(input())

for _ in range(testes):
    xy = input().split(" ")
    x = int(xy.pop(0))
    y = int(xy.pop(0))
    if x > y:
        step = -1
        start = x - 1
    else:
        step = 1
        start = x + 1
    soma_impar = 0
    for n in range(start, y, step):
        if n % 2 != 0:
            soma_impar += n
    print(soma_impar)
