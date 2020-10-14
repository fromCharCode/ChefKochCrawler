import time
from urllib.parse import urljoin
import pandas

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.chefkoch.de"


class ArticleFetcher():

    def fetch(self, url):

        link_list = []
        page = 0
        while True:

            print(url)
            # do not delete this sleep!!
            time.sleep(0.05)
            r = requests.get(url)
            soup = BeautifulSoup(r.text, "html.parser")

            '''
            for title in soup.select("main > article > a > div > h2"):
                titles.append(title.text)
            '''
            for link in soup.select("main > article > a"):
                link_list.append(link.get('href'))

            '''
            for i in range(0, len(titles)):
                links[titles[i]] = link_list[i]
            #print(links)
                #yield CrawledArticle(title, url, 1)
            '''
            soup.select("main > article > a > div > h2")
            next_buttons = []

            for item in soup.select("main > div > nav > ul > li > a"):
                next_buttons.append(item.get('href'))

            if url != next_buttons[-1]:
                next_href = next_buttons[-1]
                url = next_href
            else:
                break

            page += 1
            if page >= 50:
                page = 0
                break

        return link_list


# soup.select("head > title")
# soup.select("p > #link1") # direct child


'''
#search.pyhttps://www.crummy.com/software/BeautifulSoup/bs4/doc/
#https://gist.github.com/yoki/b7f2fcef64c893e307c4c59303ead19a
# print(link.get('href')) # http://example.com/elsi, # http://example.com/lacie
# soup.prettify()
'''
