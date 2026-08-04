import sqlite3
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "app.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row   # lets us access columns by name, like a dict
    return conn

def get_all_products():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM products").fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_product(product_id):
    conn = get_connection()
    row = conn.execute("SELECT * FROM products WHERE id = ?", (product_id,)).fetchone()
    conn.close()
    return dict(row) if row else None

def create_user(username,email,password):
    conn = get_connection()
    cursor = conn.execute(
        "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
        (username, email, password)
    )
    conn.commit()
    user_id = cursor.lastrowid
    conn.close()
    return user_id

def get_user_by_username(username):
    conn = get_connection()
    row = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
    conn.close()
    return dict(row) if row else None

def create_order(user_id, product_id, quantity, total_amount):
    conn = get_connection()
    cursor = conn.execute(
        "INSERT INTO orders (user_id, product_id, quantity, total_amount) VALUES (?, ?, ?, ?)",
        (user_id, product_id, quantity, total_amount)
    )
    conn.commit()
    order_id = cursor.lastrowid
    conn.close()
    return order_id

