import pandas as pd
import requests
from bs4 import BeautifulSoup
import os.path
from crawler import ArticleFetcher

articles = []
req = []

fetcher = ArticleFetcher()

def get_requests():
    categories = pd.read_csv("chefkoch_ouput.csv", encoding="utf8")
    for link in categories['link']:
        print("getting ", link)
        r = requests.get(link)
        req.append(r.text)


def save_request():
    df = pd.DataFrame(req)
    df.to_csv(r'requests.csv', index=False, header=False, encoding="utf8")


def load_request():
    print("loading requests")
    df = pd.read_csv("requests.csv", encoding="utf8", low_memory=False)
    for elem in df:
        req.append(elem)


def load_articles():
    print("loading article")
    df = pd.read_csv("chefkoch_articles.csv", encoding="utf8")
    articles.append(df[0])


def get_articles():
    print("getting articles")
    for r in req:
        soup = BeautifulSoup(r, "html.parser")

        for article in soup.find("article"):
            print(soup.select(".ds-rating-count"))

        # all articles
        articles.append(soup.find_all("article"))


def print_articles():
    for a in articles[0]:
        print(a, "\n\n")


def print_requests():
    print("printing requests")
    for r in req:
        soup = BeautifulSoup(r, "html.parser")
        print(soup)


def get_num_reports():
    for a in articles[0]:
        pass


if os.path.isfile("requests.csv") is True:
    load_request()
else:
    get_requests()
    save_request()


links = {}

for element in fetcher.fetch():
    links = element

df_frz = pd.DataFrame.from_dict(links)
df_frz.to_csv("Franzoesische-Rezepte.csv", index=False, header=True, encoding="utf8")


#print_requests()

#get_articles()
#print_articles()
#get_num_reports()