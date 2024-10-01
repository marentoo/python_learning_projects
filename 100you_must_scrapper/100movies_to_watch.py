#scraping simple website

from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=URL)

web_page = response.text
soup = BeautifulSoup(web_page,'html.parser')

movie_list = soup.find_all(name="h3",class_="title")
movie_titles = [item.getText() for item in movie_list]

with open("100movies_to_watch.txt", "a", encoding="utf-8") as file:
    for movie in movie_titles[::-1]:
        file.write(f"{movie}\n")