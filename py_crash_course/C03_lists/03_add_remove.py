0----------# Changin, Adding and Removing Elements

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'									# Atribui novo valor ao primeiro elemento da lista
motorcycles.append('honda')									# Adiciona novo elemento ao fim da lista


cars = []													# Cria uma lista vazia
cars.append('ford')											# 
cars.append('fiat')											# Adiciona elementos à lista	
cars.append('honda')										#	
cars.append('toyota')										#	

print(cars)

cars.insert(0, 'wolkswagen')								# Insere elemento na posição especificada em n => variavel.insert(n, novo item)
print(cars)	

del cars[1]													# Deleta o item da posição especificada de forma permanente
print(cars)		

print()

print("Função pop para aproveitar" 
	  " item de uma lista após remoção")

popped_cars = cars.pop()    								# Retira último item da lista e armazena na variável, pode especificar index nos ()
print(cars)													# Lista sem o último item após o uso de .pop()
print(popped_cars)											# Último item da lista foi atribuído a nova variável

print()
print("Deleta item da lista especificando o valor")
print(motorcycles)

motorcycles.remove('ducati')								# Deleta o item especificando o valor 
print(motorcycles)

too_expensive = 'honda'									 	# Valor 'honda' atribuído à variável too_expensive
motorcycles.remove(too_expensive)							# Deleta item especificando variável que possui item da lista atribuído

print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
