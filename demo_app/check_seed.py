import sqlite3, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(os.path.join(BASE_DIR, "app.db"))
with open(os.path.join(BASE_DIR, "seed_data.sql")) as f:
    conn.executescript(f.read())
conn.commit()

print("Users:", conn.execute("select * from users").fetchall())
print("products:", conn.execute("select * from products").fetchall())
conn.close()
