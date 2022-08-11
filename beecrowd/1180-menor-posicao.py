n = int(input())

vetor = [int(x) for x in input().split()]

menor = min(vetor)
posicao = vetor.index(menor)

print(f"Menor valor: {menor}")
print(f"Posicao: {posicao}")