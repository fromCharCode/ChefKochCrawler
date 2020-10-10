import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv


PATH = "C:\Program Files (x86)\chromedriver.exe"
BASE_URL = "https://www.chefkoch.de"
URL = "https://www.chefkoch.de/rezepte/kategorien/"


links = {}


def get_categories():
    r = requests.get(URL)

    columns = []
    soup = BeautifulSoup(r.text, "html.parser")
    for cat_col in soup.find_all("div", {"class": "category-column"}):
        columns.append(cat_col)

    for a in soup.find_all("a"):
        links[a.get('title')] = a.get('href')

    # do not check every time in loop: better performance
    del links[None]
    del links['Klassischer Flammkuchen']
    del links['Putengeschnetzeltes']
    del links['Apfelkuchen vom Blech']

    for k, v in links.items():
        links[k] = BASE_URL + v


def print_categories():
    for k, l in links.items():
        print(k, " : ", l)


def save_categories():

    dict_data = []
    for k, v in links.items():
        dict_data.append(dict(category=k, link=v))

    df = pd.DataFrame(dict_data)
    df.to_csv(r'chefkoch_ouput.csv', index=False, header=True, encoding="utf8")



def main():
    print("Starting crawler")
    get_categories()
    print_categories()
    save_categories()


if __name__ == '__main__':
    main()