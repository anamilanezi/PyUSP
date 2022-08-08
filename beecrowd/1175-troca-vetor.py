vetor = []

for i in range(20):
    vetor.append(int(input()))

for i in range(len(vetor)):
    if i == 10:
        break
    f = - (i + 1)
    subs = vetor[i]
    vetor[i] = vetor[f]
    vetor[f] = subs

for i in range(len(vetor)):
    print(f"N[{i}] = {vetor[i]}")
