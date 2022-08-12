n_coluna = int(input())
operacao = input()

matriz = []
for linhas in range(12):
    linha = []
    for colunas in range(12):
        linha.append(float(input()))
    matriz.append(linha)

coluna = []
for i in range(12):
    coluna.append(matriz[i][n_coluna])

soma = sum(coluna)
if operacao == "S":
    print(f"{soma:.1f}")
else:
    media = soma / 12
    print(f"{media:.1f}")
