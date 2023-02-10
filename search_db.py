# SELECT statement

import sqlite3

with sqlite3.connect("new.db") as conn:
    c = conn.cursor()

    c.execute("SELECT * FROM employees")

    # fetchall() retrieves all records from the query
    rows = c.fetchall()

    for r in rows:
        print(r[0], r[1])
