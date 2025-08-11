import sqlite3
import requests

conn = sqlite3.connect("products.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS personen (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    bild TEXT,
    act_price REAL
    best_price REAL
    stock INTEGER
)
""")

conn.commit()
conn.close()