import smtplib
import datetime as dt
import random

today = dt.datetime.now()
day_of_week = today.weekday()


with open("quotes.txt", mode="r") as file:
    quotes = file.read().splitlines()

my_email = "@gmail.com"
other_email = "@yahoo.com"
password = "pass"


if day_of_week == 1:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=other_email,
            msg=f"Subject:Motivational Quote\n\n{random.choice(quotes)}")

