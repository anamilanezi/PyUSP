# Functions with Outputs

def format_name(f_name, l_name):
    """ Take a first and last name and format it to return the title case version of the name"""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    full_name = f"{f_name} {l_name}"
    return full_name.title()

first_name = input("What's your first name? ")
last_name = input("What's your last name? ")

print(format_name(first_name, last_name))

# Using print doesn't allow us to store the result
def sum_of_three(n1, n2, n3):
    sum_result = n1 + n2 + n3
    print(sum_result)

sum_of_numbers = sum_of_three(1, 2, 3)  # 6

print(sum_of_numbers)                   # None