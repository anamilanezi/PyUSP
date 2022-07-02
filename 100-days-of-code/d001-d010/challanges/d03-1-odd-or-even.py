# Write a program that works out whether if a given number is an odd or even number.

number = int(input("Which number do you want to check? "))

#Write your code below this line 👇

remainder = number % 2

if (remainder == 0):
    print("This is an even number.")
else:
    print("This is an odd number.")