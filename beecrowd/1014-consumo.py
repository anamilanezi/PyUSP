km = int(input("d"))
litros = float(input("l"))

consumo = km/litros
consumo = "{:0.3f}".format(consumo)

print(f"{consumo} km/l")
