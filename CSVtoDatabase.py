import pandas as pd
from sqlalchemy import create_engine


def insert_recipe():
    engine = create_engine('sqlite:///recipe_database.db')
    read_recipe_csv = pd.read_csv("all_articles.csv")
    read_recipe_csv_df = pd.DataFrame(read_recipe_csv)
    read_recipe_csv_df.to_sql(name="all_recipes", con=engine)


insert_recipe()

''''            item["title"], item["rating"], item["rating_c"], item["recipe_time"], item[
                "difficulty"], item["person_c"], item["ingredients"], item["description"], item["tags"]
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

                
                '''
