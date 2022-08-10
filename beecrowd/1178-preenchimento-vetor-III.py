vetor = [float(input())]
print(f"N[0] = {vetor[0]:.4f}")

for i in range(1, 100):
    vetor.append(vetor[-1]/2)
    print(f"N[{i}] = {vetor[i]:.4f}")

