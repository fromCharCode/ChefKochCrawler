import pandas as pd
from Final_Data_Collector import FinalDataCollector

collector = FinalDataCollector()

articles = []
i = 0
j = 0
for elem in collector.collect():
    articles.append(elem.to_tuple())
    j += 1
    print(j)

df = pd.DataFrame(list(articles),
                  columns=['title', 'rating', 'rating_c', 'time', 'difficulty',
                           'person_c', 'ingredients', 'description', 'tags'])
df.to_csv("all_articles.csv", encoding='utf8', index=False)
