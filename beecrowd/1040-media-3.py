# A média aritmética ponderada é calculada multiplicando cada valor do conjunto de dados pelo seu peso. Depois, encontra-se a soma desses valores que será dividida pela soma dos pesos.

notas = input().split(" ")

n1 = float(notas.pop(0))
n2 = float(notas.pop(0))
n3 = float(notas.pop(0))
n4 = float(notas.pop(0))

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + n4) / 10

print(f"Media: {media:.1f}")

if (media >= 7.0):
    print("Aluno aprovado.")
elif (media < 5.0):
    print("Aluno reprovado.")
elif ((media >= 5.0) and  (media <= 6.9)):
    print("Aluno em exame.")
    exame = float(input())
    print(f"Nota do exame: {exame:.1f}")
    media_final = (exame + media) / 2
    if (media_final >= 5.0):
        print(f"Aluno aprovado.\nMedia final: {media_final:.1f}")
    elif (media_final <= 4.9):
        print(f"Aluno reprovado.\nMedia final: {media_final:.1f}")

