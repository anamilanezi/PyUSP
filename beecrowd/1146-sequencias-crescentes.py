n = int(input())
seq = []

while n != 0:
    for i in range(1, n + 1):
        seq.append(str(i))
    print(" ".join(seq))
    seq = []
    n = int(input())
