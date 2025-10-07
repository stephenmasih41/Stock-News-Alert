#IMPORTS
import requests
import smtplib

#STOCKS
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

#EMAIL
my_email = "stephenmasih39@gmail.com"
password = "nzurmsojhgplympb"

#STOCK API
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_KEY = "ST7UQKVTZJGC8K53"

#NEWS API
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = "7bffab37ff9d4eff94517b1cf79a93dd"

stock_dict = {
    "apikey": STOCK_KEY,
    "symbol": STOCK_NAME,
    "function": "TIME_SERIES_DAILY",
}

stocks = requests.get(STOCK_ENDPOINT,params=stock_dict)
stocks_data = stocks.json()['Time Series (Daily)']
dates = list(stocks_data.keys())

yesterday_stock_price = float(stocks_data[dates[0]]["4. close"])
before_yesterday_stock_price = float(stocks_data[dates[1]]["4. close"])
difference = abs(yesterday_stock_price - before_yesterday_stock_price)
percentage_difference = round((difference / float(before_yesterday_stock_price)) * 100,2)

if percentage_difference > 5:
    news_dict = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API,
        "language": "en",
        "sortBy": "popularity",
    }
    news = requests.get(NEWS_ENDPOINT, params=news_dict).json()
    news_list = news["articles"][:3]
    for news in news_list:
        msg = f"Subject:{STOCK_NAME}: 🔺 {percentage_difference}%\n\nHeadline: {news['title']}\n\nBrief: {news['description']}"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="stephenmasih39@yahoo.com",
                msg = msg.encode("utf-8")
            )
