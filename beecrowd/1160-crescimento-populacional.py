from math import floor

nt = int(input())

while nt > 0:
    compara = input().split()
    PA = int(compara[0])
    PB = int(compara[1])
    G1 = float(compara[2])
    G2 = float(compara[3])
    anos = 0
    while not PA > PB:
        anos += 1
        PA += floor(PA * (G1 / 100))
        PB += floor(PB * (G2 / 100))
        # if PA == PB:
        #     anos += 1
        if anos > 100:
            break
    if anos > 100:
        print("Mais de 1 seculo.")
    else:
        print(f"{anos} anos.")
    nt -= 1
