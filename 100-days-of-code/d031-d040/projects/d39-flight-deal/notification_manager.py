import os
import smtplib

from dotenv import load_dotenv

load_dotenv("D:/Usuarios/Usuario/ENV/.env")

FROM_EMAIL = os.getenv("SEC_EMAIL")
TO_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("SEC_PASS")

class NotificationManager:

    def send_notification(self, message):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            # Transport Layer Security: cryptographic protocols
            connection.starttls()
            connection.login(user=FROM_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=FROM_EMAIL,
                to_addrs=TO_EMAIL,
                msg="message")