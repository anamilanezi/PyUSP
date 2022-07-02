# Create a program that tells us how many days, weeks, months we have left if we live until 90 years old.

age = input("What is your current age?")

#Write your code below this line 👇

age = int(age)

years_left = 90 - age
days = years_left * 365
weeks = years_left * 52
months = years_left * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")