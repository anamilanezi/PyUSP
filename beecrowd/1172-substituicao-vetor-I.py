vetor = []

for _ in range(10):
    vetor.append(int(input()))

for i in range(len(vetor)):
    if vetor[i] <= 0:
        vetor[i] = 1
    print(f"X[{i}] = {vetor[i]}")


