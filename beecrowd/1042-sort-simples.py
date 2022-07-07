values = input().split(" ")

for i in range(len(values)):
    values[i] = int(values[i])

sorted_values= sorted(values)

for v in sorted_values:
    print(v)

print()

for v in values:
    print(v)

# sem usar a função sorted():
# for i in range(len(values)):
#     for j in range(i+1,len(values)):
#         if values[i]>values[j]:
#             values[i],values[j]=values[j],values[i]
# print(values)