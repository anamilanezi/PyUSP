numero = int(input("Digite um número: "))
verifica3 = numero % 3
verifica5 = numero % 5

if (verifica3 == 0) and (verifica5 == 0):
	print("FizzBuzz")
else:
	print(numero)