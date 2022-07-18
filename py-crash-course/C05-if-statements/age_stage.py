age = int(input("What is your age?"))

if age < 2:
	stage = 'baby'
elif 2 <= age < 4:
	stage = 'toddler'
elif 4 <= age < 13:
	stage = 'kid'
elif 13 <= age < 20:
	stage = 'teenager'
elif 20 <= age < 65:
	stage = 'adult'
elif age >= 65:
	stage = 'elder'

print(f"Your stage is: {stage}")