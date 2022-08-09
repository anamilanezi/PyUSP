n = int(input())
vetor = []
limit = 999

while len(vetor) <= limit:
    for i in range(n):
        vetor.append(i)
        print(f"N[{len(vetor) - 1}] = {vetor[i]}")
        if len(vetor) >= limit:
            break
