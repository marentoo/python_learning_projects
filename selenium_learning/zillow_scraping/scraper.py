import requests
from bs4 import BeautifulSoup



URL = "https://appbrewery.github.io/Zillow-Clone/"
HEADER = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
respond = requests.get(URL, headers=HEADER)
soup = BeautifulSoup(respond.content,"html.parser")

#TODO create a list of links
a_list = soup.find_all("a", href= True, class_ = "StyledPropertyCardDataArea-anchor")
links = [link["href"] for link in a_list] 

#TODO create a list of prices
b_list = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
# print(b_list)
all_prices_raw = [price.text for price in b_list]

def split_price(price_raw: list) -> list:
    #get rid of $
    # for i, el in enumerate(price_raw):
    #     price_raw[i] = el.split("$")[1]

    #get rid of + and everything what is right after
    for i, el in enumerate(price_raw):
        if "+" in el:
            price_raw[i] = el.split("+")[0]

    #get rid of ? and everything what is right after
        elif "/" in el:
            price_raw[i] = el.split("/")[0]

    return price_raw
prices = split_price(all_prices_raw)

addresses_raw = soup.find_all('address', {'data-test': 'property-card-addr'})
addresses = [a.text.split("\n")[1] for a in addresses_raw]
addresses = [a.split("                                  ")[1] for a in addresses]

