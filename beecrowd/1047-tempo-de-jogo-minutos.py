horas_minutos = input().split(" ")

hi = int(horas_minutos.pop(0))
mi = int(horas_minutos.pop(0))
hf = int(horas_minutos.pop(0))
mf = int(horas_minutos.pop(0))

# Método 1 (aceito)
# Converte horas em minutos e soma ao minuto inicial/final
mi += hi * 60
mf += hf * 60

# Diferença total em minutos
tempo = mf - mi

# Se a diferença for zero ou um valor negativo, adiciona 24h
if tempo <= 0:
    tempo += 24 * 60

horas = tempo // 60
minutos = tempo % 60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")

# Método 2 - Respostas corretas mas não aceito

def tempo_de_jogo(hi, mi, hf, mf):
    if hi == hf:
        horas = 24
    elif hf > hi:
        horas = hf - hi
    else:
        horas = (24 - hi) + hf

    if mi == mf:
        minutos = 0
    elif mi > mf:
        minutos = (60 - mi) + mf
        horas -= 1
    else:
        minutos = mf - mi
    print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTOS(S)")

tempo_de_jogo(hi, mi, hf, mf)
