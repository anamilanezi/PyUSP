operacao = input()

matriz = []
for linhas in range(12):
    linha = []
    for colunas in range(12):
        linha.append(float(input()))
    matriz.append(linha)

superior = []

for i in range(0, 5):
    superior.append(matriz[i][i+1:11-i])

superior_list = sum(superior, [])

soma = sum(superior_list)
if operacao == "S":
    print(f"{soma:.1f}")
else:
    media = soma / len(superior_list)
    print(f"{media:.1f}")
