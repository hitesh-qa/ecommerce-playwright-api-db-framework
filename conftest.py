import subprocess
import sys
import os
import time
import sqlite3
import urllib.request
import pytest

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEMO_APP_DIR = os.path.join(BASE_DIR, "demo_app")

def reset_database():
    conn = sqlite3.connect(os.path.join(DEMO_APP_DIR, "app.db"))
    with open(os.path.join(DEMO_APP_DIR, "seed_data.sql")) as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

def wait_for_server(url="http://127.0.0.1:5000/", timeout=10):
    start = time.time()
    while time.time() - start < timeout:
        try:
            urllib.request.urlopen(url)
            return True
        except Exception:
            time.sleep(0.5)
    return False

