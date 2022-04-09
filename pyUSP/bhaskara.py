import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

calculaDelta = (b ** 2) - (4 * a * c)

if calculaDelta < 0:
	print("esta equação não possui raízes reais")
else:
	if calculaDelta == 0:
		raiz_1 = ((- b) + (math.sqrt(calculaDelta))) / (2 * a)
		print("a raiz desta equação é", raiz_1)
	else:
		raiz_1 = ((- b) + (math.sqrt(calculaDelta))) / (2 * a)
		raiz_2 = ((- b) - (math.sqrt(calculaDelta))) / (2 * a)
		if (raiz_2 > raiz_1):
			print("as raízes da equação são", raiz_1, "e", raiz_2)
		else:
			print("as raízes da equação são", raiz_2, "e", raiz_1)






    