from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_upgrade_item_ids(driver):
    """Returns a list of item IDs available in the store."""
    item_elements = driver.find_elements(By.CSS_SELECTOR, "#store div")
    item_ids = [item.get_attribute("id") for item in item_elements]
    return item_ids

def get_affordable_upgrades(driver, item_ids):
    """Returns a dictionary of affordable upgrades with their prices as keys."""
    all_prices_elements = driver.find_elements(By.CSS_SELECTOR, "#store b")
    item_prices = []

    for price_element in all_prices_elements:
        price_text = price_element.text
        if price_text:
            cost = int(price_text.split("-")[1].strip().replace(",", ""))
            item_prices.append(cost)

    upgrades = {item_prices[i]: item_ids[i] for i in range(len(item_prices))}
    cookie_count = get_cookie_count(driver)

    affordable_upgrades = {cost: id for cost, id in upgrades.items() if cookie_count >= cost}
    return affordable_upgrades

def purchase_upgrade(driver, affordable_upgrades):
    """Purchases the most expensive affordable upgrade."""
    if affordable_upgrades:
        highest_price = max(affordable_upgrades)
        upgrade_id = affordable_upgrades[highest_price]
        driver.find_element(By.ID, upgrade_id).click()
        print(f"Purchased upgrade: {upgrade_id} for {highest_price} cookies")
