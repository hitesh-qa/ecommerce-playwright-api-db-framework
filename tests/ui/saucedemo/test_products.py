import pytest
from test_data.data import (
    VALID_USERNAME, VALID_PASSWORD,
    PRODUCT_NAME, PRODUCT_PRICE
)
from utils.helpers import Helpers

#------------Smoke Tests-----------
@pytest.mark.smoke
@pytest.mark.products
def test_home_page_loads(login_page, home_page):
    """Test inventory page loads after login."""
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    assert home_page.is_home_page_loaded(), \
    "Home page did not load after login"

@pytest.mark.smoke
@pytest.mark.products
def test_products_are_displayed( login_page, home_page):
    """Test products are visible on home page."""
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    names = home_page.get_all_product_names()
    assert len(names) > 0, \
        "No products displayed on home page"

#-------------Regression Testings -----------
@pytest.mark.regression
@pytest.mark.products
def test_products_count( login_page, home_page):
    """Test exactly 6 products are displayed."""
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    names = home_page.get_all_product_names()
    assert len(names) == 6, \
    f"Expected 6 products but got {len(names)}"

@pytest.mark.regression
@pytest.mark.products
def test_sort_products_a_to_z( login_page, home_page):
    """Test products sort A to Z correctly."""
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    home_page.sort_products("az")
    names = home_page.get_all_product_names()
    assert names == sorted(names), \
        "Products not sorted A to Z"

@pytest.mark.regression
@pytest.mark.products
def test_sort_products_price_low_to_high( login_page, home_page):
    """Test products sort by price low to high."""
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    home_page.sort_products("lohi")
    prices = home_page.get_all_product_prices()
    assert Helpers.is_price_sorted_low_to_high(prices), \
        "Products not sorted by price low to high"

@pytest.mark.regression
@pytest.mark.products
def test_add_product_to_cart_from_home( login_page, home_page):
    """Test adding product to cart from home page."""
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    home_page.add_product_by_name(PRODUCT_NAME)
    assert home_page.is_cart_badge_visible(), \
        "Cart badge not visible after adding product"
    assert home_page.get_cart_count() == "1", \
        "Cart count is not 1 after adding one product"

@pytest.mark.regression
@pytest.mark.products
def test_logout(login_page, home_page):
    """Test user can logout successfully"""
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    home_page.logout()
    assert "saucedemo.com" in login_page.get_current_url(), \
        "logout did not redirect to login page"