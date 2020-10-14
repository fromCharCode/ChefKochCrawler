import sqlite3

import pandas as pd


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn


def insert_recipe():
    try:
        test = pd.DataFrame(pd.read_csv("all_articles.csv"))

        sqliteConnection = sqlite3.connect('recipe_database')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        sqlite_insert_query = ''' INSERT INTO recipe_database()
                 VALUES() '''

        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.close()

insert_recipe()
