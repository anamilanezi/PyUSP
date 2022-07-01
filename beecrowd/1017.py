tempo = int(input())
velocidade = int(input())

distancia = tempo * velocidade

litros = distancia / 12

litros_dec = "{:.3f}".format(litros)

print(litros_dec)