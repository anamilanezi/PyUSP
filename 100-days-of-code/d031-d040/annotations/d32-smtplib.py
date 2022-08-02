import smtplib

my_email = "email@gmail.com"
other_email = "email@yahoo.com"
password = "apassword"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=other_email,
        msg="Subject:Hello\n\nThis is the body of my email")
