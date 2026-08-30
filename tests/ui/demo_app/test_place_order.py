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