num = int(input())
a = 1
b = a + 1
c = b + 1

for _ in range(num):
    print(f"{a} {b} {c} PUM")
    a += 4
    b = a + 1
    c = b + 1