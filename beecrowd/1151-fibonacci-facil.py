num = int(input())
fibo = []

for n in range(num):
    if n <= 1:
        fibo.append(n)
    else:
        s = fibo[-1] + fibo[-2]
        fibo.append(s)

fibo = [str(n) for n in fibo]

print(" ".join(fibo))

