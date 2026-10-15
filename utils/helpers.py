import os
import time
from datetime import datetime


class Helpers:
    """Utility/helper functions for the test framework."""

    @staticmethod
    def create_screenshot_name(test_name: str):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{test_name}_{timestamp}"

    @staticmethod
    def ensure_screenshots_folder():
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

    @staticmethod
    def ensure_reports_folder():
        if not os.path.exists("reports"):
            os.makedirs("reports")

    @staticmethod
    def wait(seconds: int):
        time.sleep(seconds)

    @staticmethod
    def extract_price_value(price_str: str):
        return float(price_str.replace("$", "").strip())

    @staticmethod
    def is_price_sorted_low_to_high(prices: list):
        values = [Helpers.extract_price_value(p) for p in prices]
        return values == sorted(values)

    @staticmethod
    def is_names_sorted_a_to_z(names: list):
        return names == sorted(names)

    @staticmethod
    def log(message: str):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {message}")