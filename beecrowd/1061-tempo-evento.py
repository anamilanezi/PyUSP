# di = input()
# ti = input()
# df = input()
# tf = input()

di, ti, df, tf = input(), input(), input(), input()

def converte_dia(string):
    '''Retira somente o número da string e transforma em inteiro'''
    if len(string) > 5:
        dia = int(string[-2:])
    else:
        dia = int(string[-1])
    return dia

def converte_string(time):
    '''Transforma string em lista e converte cada item em inteiro'''
    time = time.split(" : ")

    for i in range(len(time)):
        time[i] = int(time[i])
    
    return time

def converte_tempo(time):
    '''Converte o tempo em segundos'''
    time[0] *= 3600  # Hours to sec
    time[1] *= 60    # Minutes to sec   
    return sum(time)

di = converte_dia(di)
df = converte_dia(df)

ti = converte_string(ti)
sum_ti = converte_tempo(ti)

tf = converte_string(tf)
sum_tf = converte_tempo(tf)

tempo_seg = sum_tf - sum_ti

if tempo_seg <= 0:
    tempo_seg += 86400

horas = tempo_seg // 3600
resto_seg = tempo_seg % 3600

minutos = resto_seg // 60
segundos = resto_seg % 60

total_dias = df - di

if ((horas + minutos) > 0):
    if total_dias > 0:
        total_dias -=1

print(f"{total_dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")
