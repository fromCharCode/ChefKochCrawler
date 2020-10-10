import time
import requests
from bs4 import BeautifulSoup

from crawler import CrawledArticle

BASE_URL = "https://www.chefkoch.de"


class ArticleFetcher():
    def fetch(self):
        url = "https://www.chefkoch.de/rs/s0g91/Franzoesische-Rezepte.html"

        while url != "":
            print(url)
            # do not delete this sleep!!
            time.sleep(0.5)
            r = requests.get(url)
            soup = BeautifulSoup(r.text, "html.parser")

            for card in soup.select(".ds-container"):
                title = card.select(".ds-h3 .ds-heading-link")
                print(title)

                yield CrawledArticle(title, url, 1)

            url = ""
'''
            next_button = soup.select_one(".ds-page-link bi-paging-next")
            if next_button:
                next_href = next_button.attrs["href"]
                next_href = urljoin(url, next_href)
                url = next_href
            else:
                url = ""
'''