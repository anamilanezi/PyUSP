import requests
from bs4 import BeautifulSoup
import os
import smtplib
from unidecode import unidecode


from dotenv import load_dotenv

load_dotenv("D:/Usuarios/Usuario/ENV/.env")

FROM_EMAIL = os.getenv("SEC_EMAIL")
TO_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("SEC_PASS")


URL = "https://www.amazon.com/dp/B096H9RDKK/ref=sspa_dk_detail_4?psc=1&pd_rd_i=B096H9RDKK&pd_rd_w=ZiE0L&content-id=amzn1.sym.4d0fffec-3aba-4480-8fad-c6bd8f7f6b41&pf_rd_p=4d0fffec-3aba-4480-8fad-c6bd8f7f6b41&pf_rd_r=96S99SXNT4EAJ2QA7RMD&pd_rd_wg=VKmcO&pd_rd_r=58db618f-4a6b-4146-8615-944165a1f531&s=kitchen&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyMk9BVzA3RzhMWFo5JmVuY3J5cHRlZElkPUEwMjAxMDQxMVQ2RFZXS1lDTzhCJmVuY3J5cHRlZEFkSWQ9QTA0NTgwMzYzQkkwWTRYQVFUVE5GJndpZGdldE5hbWU9c3BfZGV0YWlsX3RoZW1hdGljJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
headers = {
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6",
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(URL, headers=headers)
amazon_product = response.text

soup = BeautifulSoup(amazon_product, 'html.parser')

raw_product_name = soup.find("span", id="productTitle", class_="a-size-large product-title-word-break")
product_name = raw_product_name.getText().strip().encode("utf-8")

price_div = soup.find("div", id="corePriceDisplay_desktop_feature_div", class_="celwidget")
price_str = price_div.find("span", class_="a-offscreen").getText()
price_float = float(price_str.lstrip("$"))


desired_price = 200.00

if price_float < desired_price:

    email_message = f"{product_name} is now ${price_float}\n\n{URL}"
    text = f"Subject:Amazon Price Alert!!\n\n{email_message}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # Transport Layer Security: cryptographic protocols
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs=TO_EMAIL,
            msg=text)

