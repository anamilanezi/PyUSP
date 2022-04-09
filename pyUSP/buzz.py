numero = int(input("Digite um número: "))
verifica = numero % 5

if verifica == 0:
	print("Buzz")
else:
	print(numero)