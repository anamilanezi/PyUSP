n1 = int(input("Digite um número inteiro: "))
fazComparar = True

while n1 != 0 and fazComparar:
	digito1 = n1 % 10
	n2 = n1 // 10
	digito2 = n2 % 10
	if (digito1 == digito2):
		fazComparar = False
		print("sim")
	else:
		n1 = n2
if fazComparar:
	print("não")



