nt = int(input())

for _ in range(nt):
    teste = int(input())
    divisores = 0
    for n in range((teste - 1), 0, -1):
        if teste % n == 0:
            divisores += n
    if divisores == teste:
        print(f"{teste} eh perfeito")
    else:
        print(f"{teste} nao eh perfeito")
