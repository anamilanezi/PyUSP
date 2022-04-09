def ehPrimo(x):
	div = 2
	if x == 2:
		return True
	while  x % div != 0 and x/2 > div: #---x/2 evita que o divisor alcance x
		div += 1
	if x % div == 0 and x != 1:
		return False
	else:
		return True

n = int(input("Digite um número inteiro: "))

while n > 0:
	if ehPrimo(n):
		print(n, "é primo")
	else:
		print(n, "não é primo")
	n = int(input("Digite um número inteiro: "))
