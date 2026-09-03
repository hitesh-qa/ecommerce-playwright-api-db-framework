import sqlite3
import os

from h11 import PRODUCT_ID

from pages.demo_app.product_page import ProductPage
from pages.demo_app.confirmation_page import ConfirmationPage

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
DB_PATH = os.path.join(PROJECT_ROOT, "demo_app", "app.db")

PRODUCT_ID = 1         #Wirless Mouse, seeded at $19.99
UNIT_PRICE = 19.99
QUANTITY = 2
EXPECTED_TOTAL = round(UNIT_PRICE * QUANTITY, 2)

def test_place_order_ui_api_db_match(page):
    #---------1. UI: place the order through the browser-------------
    product_page = ProductPage(page)
    product_page.goto()
    product_page.buy_product(product_id=PRODUCT_ID, quantity=QUANTITY)

    confirmation = ConfirmationPage(page)
    ui_order_id = confirmation.get_order_id()
    ui_status = confirmation.get_status()
    ui_total = confirmation.get_total()

    assert ui_status == "confirmed"
    assert ui_total == EXPECTED_TOTAL

#-----------2. API: verify the same order through the API ---------------
response = page.request.get(f"http://127.0.0.1:5000/api/orders/{ui_order_id}")
assert response.ok
api_order = response.json()

assert api_order["status"] == "confirmed"
assert api_order["total_amount"] == EXPECTED_TOTAL
assert api_order["quantity"] == QUANTITY

#---------3. DB: verify the same order directly via SQL----------
conn = sqlite3.connect(DB_PATH)
order_row = conn.execute(
    "SELECT status, total_amount, quantity FROM orders WHERE id = ? ", (ui_order_id,)
).fetchone()
payment_row = conn.execute(
    "SELECT payment_status, amount FROM payments WHERE order_id = ?", (ui_order_id,)
).fetchone()
conn.close()

