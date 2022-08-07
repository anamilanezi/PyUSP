vetor = [int(input())]

for i in range(10):
    if i > 0:
        vetor.append(vetor[i - 1] * 2)
    print(f"N[{i}] = {vetor[i]}")
