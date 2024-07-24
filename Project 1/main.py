from bs4 import BeautifulSoup

import requests
URL=("https://www.empireonline.com/movies/features/best-movies-2/")
response=requests.get(URL)
website_html=response.text

soup=BeautifulSoup(website_html, "html.parser")
#print(soup.prettify())
title=soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
print(title)

movies_title=[text.getText()  for text in title]
movies=(movies_title[::-1])

with open("movies.txt",mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
