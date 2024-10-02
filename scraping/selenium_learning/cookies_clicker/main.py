from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from cookie import get_cookie_count, click_cookie
from upgrades import get_upgrade_item_ids, get_affordable_upgrades, purchase_upgrade


def init_driver():
    """Initializes the Chrome WebDriver with specified options."""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    return driver




def main():
    driver = init_driver()
    driver.get("http://orteil.dashnet.org/experiments/cookie/")
    
    cookie = driver.find_element(By.ID, "cookie")
    item_ids = get_upgrade_item_ids(driver)

    check_interval = 5
    game_duration = 5 * 60
    end_time = time.time() + game_duration
    timeout = time.time() + check_interval

    while True:
        click_cookie(cookie, 1)

        if time.time() > timeout:
            affordable_upgrades = get_affordable_upgrades(driver, item_ids)
            purchase_upgrade(driver, affordable_upgrades)
            timeout = time.time() + check_interval

        if time.time() > end_time:
            cookies_per_second = driver.find_element(By.ID, "cps").text
            print(f"Cookies per second: {cookies_per_second}")
            break


if __name__ == "__main__":
    main()
