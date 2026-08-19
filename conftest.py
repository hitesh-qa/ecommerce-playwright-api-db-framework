import subprocess
import sys
import os
import time
import sqlite3
import urllib.request
import pytest

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEMO_APP_DIR = os.path.join(BASE_DIR, "demo_app")