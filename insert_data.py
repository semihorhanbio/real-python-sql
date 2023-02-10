# INSERT Command with Error Handler

# import the sqlite3 library
import sqlite3

# create a new database if the database doesn't already exist
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

try:
    # insert data
    cursor.execute("INSERT INTO populations VALUES('New York City', \
        'NY', 8400000)")
    cursor.execute("INSERT INTO population VALUES('San Francisco', \
        'CA', 8000000)")

    # commit the changes
    conn.commit()
except sqlite3.OperationalError as error:
    raise(error)

# close the database connection
conn.close()
