renda = float(input())

if renda <= 2000:
    IR = 'Isento'
elif renda <= 3000:
    taxa_sobre = renda - 2000
    IR = taxa_sobre * 0.08
elif renda <= 4500:
    taxa_sobre = renda - 3000
    IR = (taxa_sobre * 0.18) + (1000 * 0.08)
else:
    taxa_sobre = renda - 4500
    IR = (taxa_sobre * 0.28) + (1500 * 0.18) + (1000*0.08)

if IR == 'Isento':
    print(IR)
else:
    print(f"R$ {IR:.2f}")