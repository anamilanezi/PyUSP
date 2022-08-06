import requests
import datetime as dt
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv("D:/Usuarios/Usuario/ENV/.env")

today = dt.datetime.now().today()
yesterday = today - dt.timedelta(days=1)
day_before = yesterday - dt.timedelta(days=1)

today = today.strftime('%Y-%m-%d')
yesterday = yesterday.strftime('%Y-%m-%d')
day_before = day_before.strftime('%Y-%m-%d')

# Twilio API
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

# Stock price API
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_URL = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": STOCK_API_KEY,
}

# News API
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
news_URL = "https://newsapi.org/v2/everything"

news_parameters = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME,
    "searchIn": "description,title",
    "sortBy": "relevancy",
    "from": day_before,
    "to": today,
    "pageSize": 3
}

stock_response = requests.get(stock_URL, params=stock_parameters)
stock_response.raise_for_status()

stock_data = stock_response.json()
daily = stock_data["Time Series (Daily)"]

yesterday_closing = float(daily[yesterday]["4. close"])
day_before_closing = float(daily[day_before]["4. close"])

price_difference = yesterday_closing - day_before_closing
# yesterday_5_pct = (yesterday_closing * 5) / 100
diff_pct = (price_difference * 100) / yesterday_closing


if abs(diff_pct) >= 5:
    print("Get News!")
    news_response = requests.get(news_URL, params=news_parameters)
    news_response.raise_for_status()

    news_data = news_response.json()
    articles = news_data["articles"]

    if price_difference < 0:
        symbol = "🔻"
    else:
        symbol = "🔺"

    client = Client(account_sid, auth_token)

    for article in articles:
        headline = article["title"]
        brief = article["content"]

        message_txt = f"{STOCK} {symbol} {abs(diff_pct):.1f}%\n" \
                      f"Headline: {headline}\n" \
                      f"Brief: {brief}"

        message = client.messages \
            .create(
            body=message_txt,
            from_=os.getenv("TWILIO_NUMBER"),
            to=os.getenv("my_phone")
        )

