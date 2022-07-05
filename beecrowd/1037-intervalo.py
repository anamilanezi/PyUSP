
valor = float(input())
intervalo = [0, 25, 50, 75, 100]

if valor < 0 or valor > 100.0:
    print("Fora de intervalo")

for num in range(0, len(intervalo)):
    if valor >= intervalo[0] and valor <= intervalo[1]:
        print(f"Intervalo [{intervalo[0]},{intervalo[1]}]")
        break
    elif valor > intervalo[num] and valor <= intervalo[num+1]:
        print(f"Intervalo ({intervalo[num]},{intervalo[num+1]}]")
        break

# Resolução sem loop:
# elif (valor >= 0) and (valor <= 25):
#     print(f"Intervalo [0,25]")
# elif (valor > 25) and (valor <= 50):
#     print(f"Intervalo (25,50]")
# elif (valor > 50) and (valor <= 75):
#     print(f"Intervalo (50,75]")
# elif (valor > 75) and (valor <= 100):
#     print(f"Intervalo (75,100]")

