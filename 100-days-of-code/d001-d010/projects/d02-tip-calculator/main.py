print(
        "---------------------------------------\n"
        "$  Welcome  to  the  tip  calculator  $\n"
        "---------------------------------------")

total_bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people_to_split = int(input("How many people to split the bill? "))

# Apply the informed tip to the bill
tip = percentage_tip / 100
bill_with_tip = total_bill + (total_bill * tip)

# Split the bill
splitted_bill = bill_with_tip / people_to_split

# Round to two decimal digits
#rounded_bill = "{:.2f}".format(splitted_bill)

print(f"Each person should pay: ${splitted_bill:.2f}")
