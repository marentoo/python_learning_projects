from bs4 import BeautifulSoup
import requests

import smtplib
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# URL = "https://appbrewery.github.io/instant_pot/"
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
response = requests.get(url = URL)

soup = BeautifulSoup(response.content,'html.parser')


price = soup.find(class_="a-offscreen").get_text()
price = float(price.split("$")[1])

title = soup.find(id="productTitle").get_text().strip()

BUY_PRICE = 100

if price < BUY_PRICE:
    message = f"{title} is on sale for {price}!"
else:
    message = None
# print(message)


    
    # with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
    #     connection.starttls()
    #     result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
    #     connection.sendmail(
    #         from_addr=os.environ["EMAIL_ADDRESS"],
    #         to_addrs=os.environ["EMAIL_ADDRESS"],
    #         msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
    #     )