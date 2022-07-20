n = int(input())
total = 0
testes = {
    "C": 0,
    "R": 0,
    "S": 0,
}
percentual = []


for _ in range(n):
    teste = input().split(" ")
    testes[teste[-1]] += int(teste[0])
    total += int(teste[0])


for value in testes.values():
    pct = (value * 100)/ total
    percentual.append(pct)


print(f"Total: {total} cobaias")
print(f"Total de coelhos: {testes['C']}")
print(f"Total de ratos: {testes['R']}")
print(f"Total de sapos: {testes['S']}")
print(f"Percentual de coelhos: {percentual[0]:.2f} %")
print(f"Percentual de ratos: {percentual[1]:.2f} %")
print(f"Percentual de sapos: {percentual[2]:.2f} %")