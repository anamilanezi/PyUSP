n_linha = int(input())
operacao = input()

matriz = []
for linhas in range(12):
    linha = []
    for colunas in range(12):
        linha.append(float(input()))
    matriz.append(linha)

linha = matriz[n_linha]
soma = sum(linha)
if operacao == "S":
    print(f"{soma:.1f}")
else:
    media = soma / 12
    print(f"{media:.1f}")