#scraping simple website
date = input("what year you would like to travel to? (YYY-MM-DD): ")

from bs4 import BeautifulSoup
import requests

URL = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(url=URL)

web_page = response.text
soup = BeautifulSoup(web_page,'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

print(song_names)
with open(f"100songs_to_listen_{date}.txt", "a", encoding="utf-8") as file:
    for song in song_names:
        file.write(f"{song}\n")
