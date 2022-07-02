# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

#Write your code below this line 👇
bmi = weight / (height ** 2)
rounded_bmi = round(bmi)

if rounded_bmi < 18.5:
    print(f"Your BMI is {rounded_bmi}, you are underweight.")
elif rounded_bmi < 25:
    print(f"Your BMI is {rounded_bmi}, you have a normal weight.")
elif rounded_bmi < 30:
    print(f"Your BMI is {rounded_bmi}, you are slightly overweight.")
elif rounded_bmi < 35:
    print(f"Your BMI is {rounded_bmi}, you are obese.")
else:
    print(f"Your BMI is {rounded_bmi}, you are clinically obese.")