import sqlite3
from datetime import datetime

with sqlite3.connect("new.db") as conn:
    c = conn.cursor()
    rows = c.execute("SELECT model, COUNT(make) FROM orders GROUP BY model;").fetchall()
    for r in rows:
        print(r)
