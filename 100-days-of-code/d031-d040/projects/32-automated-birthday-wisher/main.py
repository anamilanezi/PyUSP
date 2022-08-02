import datetime as dt
import pandas as pd
import random
import smtplib

my_email = "email@gmail.com"
password = "pass123"

letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
birthday_data = pd.read_csv("birthdays.csv")

now = dt.datetime.now()
day = now.day
month = now.month

for (index, row) in birthday_data.iterrows():
    if row.month == month and row.day == day:

        name = row['name']
        email = row['email']

        with open(f"letter_templates/{random.choice(letters)}") as letter_file:
            letter = letter_file.read()

        email_msg = letter.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject:Happy Birthday {name.title()}!\n\n{email_msg}")
