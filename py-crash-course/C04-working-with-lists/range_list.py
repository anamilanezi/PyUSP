# Função range para criar sequência numérica

for value in range (1, 5):				# Imprimir números de 1 a 4 (não inclui 5)
	print(value)

# Criar uma lista usando list(range())

numbers = list(range(1,5))
print(numbers)

# Terceiro argumento para pular números

even_numbers = list(range(2,11,2)) # O terceiro argumento faz com que pule os números de dois em dois
print(even_numbers)

odd_numbers = list(range(1,10,2))
print(odd_numbers)

tabuada_de_tres = list(range(0,31,3))
print(even_numbers)

# Criar uma lista dos 10 primeiros números elevados ao quadrado usando range e loop

squares = []				# Cria a lista vazia que vai ser alimentada pela loop
for value in range(1,11):	# Cria um loop que percorre os números de 1 à 10 atribuindo à value
	square = value ** 2		# Cálculo da exponenciação é atribuído à square
	squares.append(square)	# Cada valor calculado é adicionado à lista vazia criada antes da loop
print(squares)

# Mesma lista criada sem uma variável para square

squares = []
for value in range(1,11):
	squares.append(value**2)		# O valor é calculado e adicionado à lista sem uma variável intermediária

print(squares)

# Lista compreensiva cria a mesma lista diretamente na criação da lista usando for

squares = [value**2 for value in range(1,11)]