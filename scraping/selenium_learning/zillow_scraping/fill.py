from selenium import webdriver
from selenium.webdriver.common.by import By
from scraper import HEADER
from scraper import links, prices, addresses
import time


URL ="https://docs.google.com/forms/d/e/1FAIpQLSfRg0KKAxzjNcM7a3yKGwRX6_NAoCjW4KEv8b4Rwd5fRSIDoQ/viewform?usp=sf_link"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_options)
driver.get(	URL)

address = addresses[0]
a = driver.find_element(by=By.XPATH, 
                    value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
a.send_keys(address)

# driver.close()