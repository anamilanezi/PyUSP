# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# combine names
combined_names = name1 + name2

# turn names into lowercase
lower_case_names = combined_names.lower()

### Refactor in the future using list and for loop ###

# count the letters from the word "TRUE"
t = lower_case_names.count('t') 
r = lower_case_names.count('r') 
u = lower_case_names.count('u') 
e = lower_case_names.count('e') 

true = t + r + u + e

# count the letters from the word "LOVE"
l = lower_case_names.count('l')  
o = lower_case_names.count('o')  
v = lower_case_names.count('v') 

love = l + o + v + e

score = int(str(true) + str(love))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")