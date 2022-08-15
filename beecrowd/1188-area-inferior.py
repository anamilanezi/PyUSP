operacao = input()

matriz = []
for linhas in range(12):
    linha = []
    for colunas in range(12):
        linha.append(float(input()))
    matriz.append(linha)

inferior = []
col = 2

for i in range(7, 12):
    inferior.append(matriz[i][i-col:i])
    col += 2

inferior_list = sum(inferior, [])

soma = sum(inferior_list)
if operacao == "S":
    print(f"{soma:.1f}")
else:
    media = soma / len(inferior_list)
    print(f"{media:.1f}")
