positives = True
while positives:
    mn = input().split(" ")
    m = int(mn.pop(0))
    n = int(mn.pop(0))
    if m <= 0 or n <= 0:
        positives = False
        continue
    seq = []
    soma = 0
    if m > n:
        start = n
        stop = m + 1
    else:
        start = m
        stop = n + 1
    for i in range(start, stop):
        soma += i
        seq.append(str(i))
    saida = f'{" ".join(seq)} Sum={soma}'
    print(saida)

