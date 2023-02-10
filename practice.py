import sqlite3
from datetime import datetime

with sqlite3.connect("new.db") as conn:
    c = conn.cursor()
