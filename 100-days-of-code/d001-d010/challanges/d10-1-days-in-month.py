# Create a function called days_in_month() which will take a year and a month as inputs and it will
# use this information to work out the number of days in the month, then return that as the output

def is_leap(year):
    """Return True if it is a leap year and False if it is not"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    """Checks if the year is leap or not and return the total days of month."""
    month_position = month - 1
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    
    if month > 12 or month < 1:
        return "Invalid month."
    if is_leap(year) and month == 2:
            return 29
    else:
        days = month_days[month_position]
        return days

#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)







