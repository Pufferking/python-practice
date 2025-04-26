import requests
from twilio.rest import Client
#codes are from trial accounts no actual valuable codes are listed
stock_api_key = "L9X793O6HTBDS9Z4"
news_api_key = "92074fd66c6c4b308cbd1f5169cf55a8"
twilio_sid = "AC8d19790864c13b5104a231bb0e70a2f4"
twilio_auth_token = "986264e071e42c2caa45625ef7ed64be"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": stock_api_key,
    "outputsize": 20
}

response = requests.get(url = "https://www.alphavantage.co/query", params = stock_parameters)
stock_price_data = response.json()
data = stock_price_data["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]["4. close"]
day_before_yesterday_data = data_list[1]["4. close"]
difference = float(yesterday_data) - float(day_before_yesterday_data)
dif_percent = (abs(difference) / float(yesterday_data)) * 100


## STEP 2: Use https://newsapi.org
news_parameters = {
    "apiKey": news_api_key,
    "qInTitle": "Tesla"
}
if dif_percent > 5:
    response_2 = requests.get(url = "https://newsapi.org/v2/everything", params = news_parameters)
    news = response_2.json()
    articles = news["articles"]
    three_articles  = articles[:3]
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    if difference > 0:
        change = "🔺"
    elif difference < 0:
        change = "🔻"

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
    formatted_articles = [f"TSLA {change}{round(dif_percent)}%\nHeadline: {article['title']}\nBrief: {article['description']}" for article in three_articles]
    client = Client(twilio_sid, twilio_auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+16672740765",
            to="recipient number"
        )


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

