#  Write a function that checks whether if the number passed into it is a prime number or not.

#Write your code below this line 👇
def prime_checker(number):
    is_prime = True 
    if (number == 1):
        is_prime = False    
    for i in range(2, number):
        if ((number % i) == 0):
            is_prime = False
            break
    if not is_prime:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
