nt = int(input())

for _ in range(nt):

    teste = int(input())

    for t in range(2, teste + 1):
        if t == teste:
            print(f"{teste} eh primo")
        elif teste % t == 0:
            print(f"{teste} nao eh primo")
            break


