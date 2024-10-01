from selenium import webdriver
from selenium.webdriver.common.by import By
import time





def get_cookie_count(driver):
    """Returns the current number of cookies as an integer."""
    money_element_text = driver.find_element(By.ID, "money").text
    return int(money_element_text.replace(",", ""))






def click_cookie(cookie_element, duration):
    """Clicks the cookie for the specified duration in seconds."""
    end_time = time.time() + duration
    while time.time() < end_time:
        cookie_element.click()