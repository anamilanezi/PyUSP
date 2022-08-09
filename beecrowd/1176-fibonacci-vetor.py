nt = int(input())

for _ in range(nt):
    fibo = []
    fn = int(input())
    for i in range(fn + 1):
        if i <= 1:
            fibo.append(i)
        else:
            s = fibo[-1] + fibo[-2]
            fibo.append(s)
    print(f"Fib({fn}) = {fibo[fn]}")

# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368