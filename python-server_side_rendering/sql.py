import sqlite3

conn = sqlite3.connect("products.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    category TEXT NOT NULL
)
""")

products = [
    (1, "Laptop", 799.99, "Electronics"),
    (2, "Coffee Mug", 15.99, "Home Goods")
]

cur.executemany(
    "INSERT OR REPLACE INTO Products (id, name, price, category) VALUES (?, ?, ?, ?)",
    products
)

conn.commit()
conn.close()
