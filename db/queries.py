CREATETABLE_store = """
CREATE TABLE IF NOT EXISTS store (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name_product TEXT,
category TEXT,
size TEXT,
price TEXT,
product_id TEXT,
photo TEXT
)
"""


INSERT_store = """
INSERT INTO store (name_product, category, size, price, product_id, photo)
VALUES (?, ?, ?, ?, ?, ?)
"""