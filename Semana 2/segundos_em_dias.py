#S2O2 - Cria programa que recebe segundos e transforma esse valor em dias, horas e minutos.

entra_segundos = int(input("Por favor, entre com o número de segundos que deseja converter:"))
segundos_dia = 86400
segundos_hora = 3600
segundos_minuto = 60

dias = entra_segundos // segundos_dia          #transforma segundos em dias
resto_dia = entra_segundos % segundos_dia      #armazena o restante de segundos que não completam um dia
hora = resto_dia // segundos_hora              #transforma segundos em horas
resto_hora = resto_dia % segundos_hora         #armazena o restante de segundos que não completam uma hora
minutos = resto_hora // segundos_minuto        #transforma segundos em minutos
segundos = resto_hora % segundos_minuto        #armazena os segundos que não completaram um minuto

print(dias, "dias,", hora, "horas,", minutos, "minutos e", segundos, "segundos.")