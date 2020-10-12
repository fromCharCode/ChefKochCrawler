class CrawledArticle():
    def __init__(self, title="Init_title",
                 rating=0.0, rating_c=0,
                 num_rep=0, time=0,
                 difficulty="normal", person_c=1,
                 ingredients=[], description="", tags=[]):
        self.rating_count = rating_c
        self.time = time
        self.difficulty = difficulty
        self.person_count = person_c
        self.ingredients = ingredients
        self.description = description
        self.tags = tags
        self.rating = rating
        self.title = title
        self.num_rep = num_rep
