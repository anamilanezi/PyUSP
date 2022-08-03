a = 1
b = 1
s = 1

for n in range(2, 40, 2):
    a = 1 + n
    b *= 2
    s += a / b

print(f"{s:.2f}")
