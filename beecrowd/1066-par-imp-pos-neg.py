numbers = []
i = 5
imp = 0
par = 0
pos = 0
neg = 0

while i > 0:
    numbers.append(int(input()))
    i -= 1

for n in numbers:
    if n % 2 == 0:
        par += 1
    else:
        imp += 1
    if n > 0:
        pos += 1
    elif n < 0:
        neg += 1

print(f"{par} valor(es) par(es)")
print(f"{imp} valor(es) impar(es)")
print(f"{pos} valor(es) positivo(s)")
print(f"{neg} valor(es) negativo(s)")
