# JOINing data from multiple tables

import sqlite3

with sqlite3.connect("new.db") as conn:
    c = conn.cursor()

    # retrieve data
    c.execute("""
                SELECT DISTINCT population.city, population.population, regions.region
                FROM population, regions
                WHERE population.city = regions.city
                ORDER BY population.city;
    """)

    rows = c.fetchall()
    for r in rows:
        print("City: " + r[0])
        print("Population: " + str(r[1]))
        print("Region: " + r[2])
        print("")
