class CrawledArticle():
    def __init__(self, title,
                 rating, rating_c, time,
                 difficulty, person_c,
                 ingredients, description, tags):
        self.rating_count = rating_c
        self.time = time
        self.difficulty = difficulty
        self.person_count = person_c
        self.ingredients = ingredients
        self.description = description
        self.tags = tags
        self.rating = rating
        self.title = title

        print(
            str(self.title), "(" + str(self.rating) + "/" + str(self.rating_count) + "):" + "\n" +
            "time: " + str(self.time) + " difficulty: " + str(self.difficulty) + "\n" +
            "Ingredients for " + str(self.person_count) + " persons: " + "\n" +
            str(self.ingredients), "\n" +
            "How to: " + str(self.description) + "\n" +
            str(self.tags) + "\n\n"
            )
