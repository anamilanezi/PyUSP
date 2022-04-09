entra_segundos = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(entra_segundos)

dias = total_segs // 86400
tempo_restante = total_segs % 86400
horas = tempo_restante // 3600
segs_restantes = tempo_restante % 3600
minutos = segs_restantes // 60
segs_final = segs_restantes % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segs_final, "segundos.")