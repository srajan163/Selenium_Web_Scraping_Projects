from bs4 import BeautifulSoup

import requests
responce=requests.get("https://news.ycombinator.com/news")
yc_webpage=responce.text

soup=BeautifulSoup(yc_webpage,"html.parser")
# print(soup.prettify())
td_element = soup.find('span', class_='titleline')
ai_news = td_element.find('a')

# ai_news=soup.find(name="span",class_="titleline")
artical_text=ai_news.text
artical_link=ai_news["href"]
artical_upvote=soup.find(name="span",class_="score").getText()
print(artical_text)
print(artical_link)
print(artical_upvote)

# with open("website.html",encoding="utf8") as file:
#     content=file.read()
#
#
# soup=BeautifulSoup(content,'html.parser')
# #print(soup.prettify())
#
# name=soup.select_one(selector="#name")
# print(name)
#
# a_taggs=soup.find_all("h3",class_="heading")
# print(a_taggs)