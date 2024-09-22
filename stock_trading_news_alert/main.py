import requests
from config import news_api_key, stock_api_key, twilio_api_key,account_sid
from config import STOCK_NAME, COMPANY_NAME, STOCK_ENDPOINT, NEWS_ENDPOINT, THRESHOLD, FROM_NUMBER, DEST_NUMBER
from twilio.rest import Client


def get_stock_data():
    stock_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey":stock_api_key,
    }
    response = requests.get(url = STOCK_ENDPOINT, params=stock_parameters)
    data = response.json()["Time Series (Daily)"]
    return data


def transform_stock_data(data_list):
    yesterday_closing_price = data_list[0]["4. close"]
    day_before_yesterday_closing_price = data_list[1]["4. close"]
    difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
    percentage_difference = round((difference/float(yesterday_closing_price))* 100)
    return difference, percentage_difference


def format_articles(difference, percentage_difference):
    up_down=None
    if difference > 0:
        up_down="🔺"
    else:
        up_down = "🔻"

    news_parameters = {
        "apiKey": news_api_key,
        "qInTitle": COMPANY_NAME,
    }

    r = requests.get(url = NEWS_ENDPOINT, params = news_parameters)
    data_news =  r.json()["articles"]
    three_articles = data_news[:3]


    formatted_article = [f"{STOCK_NAME}: {up_down}{percentage_difference}%\nHeadline: {article ['title']}. \nBrief: {article ['description']}" for article in three_articles]
    return formatted_article


def send_sms(difference, percentage_difference):
    formatted_article = format_articles(difference, percentage_difference)

    client = Client(account_sid, twilio_api_key)
    
    for article in formatted_article:
        message = client.messages.create(
            body=article,
            from_= FROM_NUMBER,
            to=DEST_NUMBER,
        )


data = get_stock_data()
data_list = [value for (key,value) in data.items()]
difference, percentage_difference = transform_stock_data(data_list) 

if abs(percentage_difference) >= THRESHOLD:
    send_sms(difference, percentage_difference)


