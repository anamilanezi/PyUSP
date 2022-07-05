x1y1 = (input()).split()
x2y2 = (input()).split()

x1 = float(x1y1.pop(0))
y1 = float(x1y1.pop(0))

x2 = float(x2y2.pop(0))
y2 = float(x2y2.pop(0))

distancia = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1/2)

distancia = "{:0.4f}".format(distancia)

print(distancia)