import sqlite3
from random import sample

with sqlite3.connect("newnum.db") as conn:
    c = conn.cursor()
    c.execute("DROP TABLE if exists randomNumbers")
    c.execute("CREATE TABLE randomNumbers(numbers INT)")

    # create 100 random integers
    random_list = sample(range(0, 101), 100)

    # change random_list to list of tuples for executemany method
    random_tuple = [(i,) for i in random_list]

    # insert numbers into table
    c.executemany("INSERT INTO randomNumbers VALUES(?)", random_tuple)
