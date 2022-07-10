horas = input().split(" ")

inicial = int(horas.pop(0))
final = int(horas.pop(0))

def tempo_de_jogo(hora_inicial, hora_final):
    if hora_inicial == hora_final:
        tempo = 24
    elif hora_final > hora_inicial:
        tempo = hora_final - hora_inicial
    else:
        tempo = (24 - hora_inicial) + hora_final

    print(f"O JOGO DUROU {tempo} HORA(S)")

tempo_de_jogo(inicial, final)
