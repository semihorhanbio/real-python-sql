# SQLite Functions

import sqlite3

with sqlite3.connect("new.db") as conn:
    c = conn.cursor()

    # create a dictionary of sql queries
    sql = {'average': "SELECT AVG(population) FROM population",
           'maximum': "SELECT MAX(population) FROM population",
           'minimum': "SELECT MIN(population) FROM population",
           'sum': "SELECT SUM(population) FROM population",
           'count': "SELECT COUNT(population) FROM population"}

    # run each sql query item in dictionary
    for key, value in sql.items():

        # fetchone() retrieves one record from the query
        result = c.execute(value).fetchone()

        # output the result to screen
        print(key + ':', result[0])
