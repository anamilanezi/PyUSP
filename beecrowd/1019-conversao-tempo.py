segundos_entrada = int(input())

horas = segundos_entrada // 3600
resto = segundos_entrada % 3600

minutos = resto // 60
segundos = resto % 60

print(f"{horas}:{minutos}:{segundos}")
