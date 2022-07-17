n = int(input())
numbers = []
interval = list(range(10, 21))
n_in = 0
n_out = 0

while n > 0:
    numbers.append(int(input()))
    n -= 1

for n in numbers:
    if n in interval:
        n_in += 1
    else:
        n_out += 1

print(f"{n_in} in")
print(f"{n_out} out")