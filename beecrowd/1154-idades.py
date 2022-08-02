le_idade = True
idades = []

while le_idade:
    idade = int(input())
    if idade < 0:
        le_idade = False
    else:
        idades.append(idade)


print(f"{(sum(idades)/len(idades)):.2f}")
