num = input().split()

x = int(num[0])
y = int(num[1])

a = 0
nums = []
while a < y:
    for _ in range(x):
        a += 1
        if a > y:
            break
        nums.append(str(a))

    print(" ".join(nums))
    nums = []



