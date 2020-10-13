import os
import time
from urllib.parse import urljoin

import pandas as pd
import re

import requests
from bs4 import BeautifulSoup

from crawler import CrawledArticle


class FinalDataCollector():

    def collect(self):
        url_list = ['https://www.chefkoch.de/rezepte/3017351454519857/KFC-Coleslaw.html']
        df = pd.read_csv("all_recipe_links.csv")

        for link in df["https://www.chefkoch.de/rezepte/3017351454519857/KFC-Coleslaw.html"]:
            url_list.append(link)

        print(url_list)

        while url_list:
            url = url_list.pop(0)
            time.sleep(0.5)
            r = requests.get(url)

            soup = soup = BeautifulSoup(r.text, "html.parser")

            # get rating
            for strong in soup.select("main > article > div > div > div > a > div > span > strong"):
                rating = strong.text

            # get amount of raters
            p = re.compile("[0-9]+")
            for span in soup.select("main > article > div > div > div > a > div > span > span"):
                if p.findall(span.text):
                    nums = p.findall(span.text)[0]

            # get name
            for name in soup.select("main > article > div > h1"):
                name = name.text

            # get time
            p2 = re.compile("[0-9]+ Min.")
            for s in soup.find_all("span", {"class": "recipe-preptime"}):
                if p2.findall(s.text):
                    t = p2.findall(s.text)[0]

            # get difficulty
            p3 = re.compile("[a-z]+")
            for s in soup.find_all("span", {"class": "recipe-difficulty"}):
                if p3.findall(s.text):
                    difficulty = p3.findall(s.text)[0]

            # get amount of portions
            portion_amount = soup.find('input', {'class': 'ds-input'}).get('value')

            # get ingredients
            ingredients = []
            a_l = []
            i_l = []
            amounts = soup.select("main > article > table > tbody > tr > td.td-left")
            for amount in amounts:
                test = amount.text.strip()
                test = test.replace("   ", "")
                test = test.replace(" ½", ",5")
                test = test.replace("½", "0,5")
                test = test.replace(" ¼", ",25")
                test = test.replace("¼", "0,25")
                test = test.replace(" ⅛", ",125")
                test = test.replace("⅛", "0,125")
                test = test.replace("  ", " ")
                test = os.linesep.join([s for s in test.splitlines() if s])
                if not test:
                    test = '0'
                a_l.append(test)

            ings = soup.select("main > article > table > tbody > tr > td.td-right")
            for ing in ings:
                i = ing.text
                i = os.linesep.join([s for s in i.splitlines() if s])
                i_l.append(i)

            for i in range(0, len(amounts)):
                ingredients.append((a_l[i], i_l[i]))

            # get instructions
            recipe_instruction = soup.select_one(
                "main > article.ds-box.ds-grid-float.ds-col-12.ds-col-m-8.ds-or-3 > div.ds-box").text.strip()
            recipe_instruction = os.linesep.join([s for s in recipe_instruction.splitlines() if s])

            # get tags
            tags_source = soup.select("main > article > div > amp-carousel > div")
            tags = []
            for tag in tags_source:
                tags.append(tag.text.split()[0])


            yield CrawledArticle(name, rating, nums, t, difficulty, portion_amount, ingredients, recipe_instruction, tags)


'''
#search.pyhttps://www.crummy.com/software/BeautifulSoup/bs4/doc/
#https://gist.github.com/yoki/b7f2fcef64c893e307c4c59303ead19a
# print(link.get('href')) # http://example.com/elsi, # http://example.com/lacie
# soup.prettify()
'''
