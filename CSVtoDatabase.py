import sqlite3
import time
import ast
import pandas as pd



def insert_recipe(title, rating, rating_c, recipe_time, difficulty, person_c, ingredients, description, tags):
    try:

        sqliteConnection = sqlite3.connect('recipe_database')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        sqlite_insert_with_param = """ INSERT INTO all_recipes(title, rating, rating_c, recipe_time, difficulty, person_c, ingredients, description, tags)
                             VALUES(?,?,?,?,?,?,?,?,?); """

        data_tuple = (title, rating, rating_c, recipe_time, difficulty, person_c, ingredients, description, tags)
        cursor.executemany(sqlite_insert_with_param, (data_tuple,))
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)

    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")


from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)
test = pd.read_csv("all_articles.csv", chunksize=1)
test2 = pd.DataFrame(test)
test2.to_sql(name="test", con=engine)

print(test2)

i = 0

for item in test:
    time.sleep(3)
    i += 1
    """
    title = item["title"]
    rating = item["rating"]
    rating_c = item["rating_c"]
    recipe_time = item["recipe_time"]
    difficulty = item["difficulty"]
    person_c = item["person_c"]
    ingredients = item["ingredients"]
    description = item["description"]
    tags = item["tags"]
"""



    # print(title)
    # print(rating)
    # print(tags)

    #insert_recipe(title, rating, rating_c, recipe_time, difficulty, person_c, ingredients, description, tags)

#insert_recipe('test', 4.5, 4, 10, 'test', 4, 'test', 'test', 'test')

''''            item["title"], item["rating"], item["rating_c"], item["recipe_time"], item[
                "difficulty"], item["person_c"], item["ingredients"], item["description"], item["tags"]'''
