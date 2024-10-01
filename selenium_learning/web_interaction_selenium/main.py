from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_options)

URL = "https://python.org/"
driver.get(URL)

upcoming_events_raw = driver.find_element(By.XPATH, value = '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
# print(upcoming_events_raw.text)
a_list = []
for line in upcoming_events_raw.text.split("\n"):
    a_list.append(line)
# print(a_list)

event_names = []
event_times = []

for i, x in enumerate(a_list):
    if i%2 != 0:
        event_names.append(a_list[i])
    elif i%2 == 0:
        event_times.append(a_list[i])
print(event_names)
print("")
print(event_times)

events = {}

for n in range(len(event_names)):
    events[n] = {
        "time": event_times[n],
        "name": event_names[n]
    }
print(events)
# for i in range(len(a_list)):
#     a_dictionary[i] = {
#         "time": event_times,
#         "name" :event_names
#     }

driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_options)
URL = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(URL)
num_articles = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(num_articles.text)
driver.quit()