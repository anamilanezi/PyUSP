# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#Write your code below this line 👇

height = float(height)
weight = float(weight)

bmi = weight / (height ** 2)

print(int(bmi))