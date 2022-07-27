
novo_grenal = True
grenais = []
while novo_grenal:
    grenal = [int(i) for i in input().split()]
    grenais.append(grenal)
    print("Novo grenal? (1-sim 2-nao)")
    resposta = int(input())
    if resposta == 2:
        novo_grenal = False

print(f"{len(grenais)} grenais")
inter = 0
gremio = 0
empate = 0

for grenal in grenais:
    if grenal[0] > grenal[1]:
        inter += 1
    elif grenal[1] > grenal[0]:
        gremio += 1
    else:
        empate += 1
print(f"Inter:{inter}")
print(f"Gremio:{gremio}")
print(f"Empates:{empate}")

if inter > gremio:
    print("Inter venceu mais")
elif gremio > inter:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
