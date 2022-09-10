import requests
from datetime import date
from datetime import timedelta
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
STOCK_API_KEY = os.getenv('STOCK_API_KEY')
TWILIO_ACCOUNT_SID = os.geten('TWILIO_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE')
MY_PHONE_NUMBER = os.getenv('MY_PHONE')
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# # STEP 1: Use https://newsapi.org/docs/endpoints/everything When STOCK price increase/decreases by 5% between
# yesterday and the day before yesterday then print("Get News"). HINT 1: Get the closing price for yesterday and the
# day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive
# difference is 20. HINT 2: Work out the value of 5% of yesterday's closing stock price.

# Can use datetime too if accuracy needed
# today = date.today()
# yesterday = str(today - timedelta(days=1))
# day_before_yesterday = str(today - timedelta(days=2))
# # print(f"Today is {today}\nYesterday was {yesterday}\nTwo days before was {day_before_yesterday}")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "interval": "60min",
    "apikey": STOCK_API_KEY,

}

news_params = {
    "qInTitle": COMPANY_NAME,
    # "from": yesterday,
    "language": "en",
    # "sortBy": "relevancy",
    "apikey": NEWS_API_KEY,
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]

stock_data_list = [value for (key, value) in stock_data.items()]
# yesterday_stock_data = stock_data_list[0]

yesterday_data = stock_data_list[0]
yesterday_stock_closing_price = float(yesterday_data["4. close"])

two_days_before_data = stock_data_list[1]
two_days_before_closing_price = float(two_days_before_data["4. close"])

stock_difference = yesterday_stock_closing_price - two_days_before_closing_price
percentage = round(stock_difference / yesterday_stock_closing_price) * 100

up_down = None
if stock_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

if abs(percentage) > 1:
    print("Get News")
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"][:3]
    formatted_articles = [f"{STOCK_NAME}: {up_down}{percentage}%\nHeadline: {article['title']}\nBrief: {article['content']}\n"
                          f"URL: {article['url']}" for article in news_data]
    print(formatted_articles)

    for article in formatted_articles:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages \
            .create(
            body=article,
            from_=TWILIO_PHONE_NUMBER,
            to=MY_PHONE_NUMBER
        )

        print(message.status)

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
# HINT 1: Think about using the Python Slice Operator


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
# HINT 1: Consider using a List Comprehension.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
