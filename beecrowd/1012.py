values = (input(" ")).split()

A = float(values.pop(0))
B = float(values.pop(0))
C = float(values.pop(0))

pi = 3.14159

# Área do triângulo retângulo A = base | C = altura
triangulo = (A * C) / 2
triangulo = "{:0.3f}".format(triangulo)

print(f"TRIANGULO: {triangulo}")

# Área do círculo C = raio
circulo = pi * (C ** 2)
circulo = "{:0.3f}".format(circulo)
print(f"CIRCULO: {circulo}")

# Área do trapézio A, B = base | C = altura
trapezio = ((A + B) * C) / 2
trapezio = "{:0.3f}".format(trapezio)
print(f"TRAPEZIO: {trapezio}")


# Área do quadrado B = lado
quadrado = B ** 2
quadrado = "{:0.3f}".format(quadrado)
print(f"QUADRADO: {quadrado}")

# Área do retângulo A, B = lados
retangulo = A * B
retangulo = "{:0.3f}".format(retangulo)
print(f"RETANGULO: {retangulo}")
