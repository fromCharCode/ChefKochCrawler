import time
from urllib.parse import urljoin
import pandas as pd
import re

import requests
from bs4 import BeautifulSoup

from crawler import CrawledArticle


df = pd.read_csv("all_recipe_links.csv")

print(df.head())
url = "https://www.chefkoch.de/rezepte/1498571255339854/Wildschweingulasch.html"
            # do not delete this sleep!!
time.sleep(0.5)
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
# while links has next
# ...code ... yield CrawledArticle

# get rating
for strong in soup.select("main > article > div > div > div > a > div > span > strong"):
    rating = strong.text
print(rating)

# get amount of raters
p = re.compile("[0-9]+")
for span in soup.select("main > article > div > div > div > a > div > span > span"):
    if p.findall(span.text):
        nums = p.findall(span.text)[0]
print(nums)


# get name
for name in soup.select("main > article > div > h1"):
    name = name.text
print(name)


# get time
p2 = re.compile("[0-9]+ Min.")
for s in soup.find_all("span", {"class": "recipe-preptime"}):
    if p2.findall(s.text):
        time = p2.findall(s.text)[0]
print(time)


# get difficulty
p3 = re.compile("[a-z]+")
for s in soup.find_all("span", {"class": "recipe-difficulty"}):
    if p3.findall(s.text):
        difficulty = p3.findall(s.text)[0]
print(difficulty)

# get amount of portions

# get ingredients

# get making of

# get tags

'''
            for title in soup.select("main > article > a > div > h2"):
                titles.append(title.text)

            for link in soup.select("main > article > a"):
                link_list.append(link.get('href'))

            for i in range(0, len(titles)):
                links[titles[i]] = link_list[i]
            #print(links)
                #yield CrawledArticle(title, url, 1)
'''

            #soup.select("main > article > a > div > h2")
            #next_buttons = []
'''
            for item in soup.select("main > div > nav > ul > li > a"):
                next_buttons.append(item.get('href'))

            if url != next_buttons[-1]:
                next_href = next_buttons[-1]
                url = next_href
            else:
                break

        return link_list


# soup.select("head > title")
# soup.select("p > #link1") # direct child

'''
'''
#search.pyhttps://www.crummy.com/software/BeautifulSoup/bs4/doc/
#https://gist.github.com/yoki/b7f2fcef64c893e307c4c59303ead19a
# print(link.get('href')) # http://example.com/elsi, # http://example.com/lacie
# soup.prettify()
'''
