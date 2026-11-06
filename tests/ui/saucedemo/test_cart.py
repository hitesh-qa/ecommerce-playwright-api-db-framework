import pytest
from test_data.data import (
    VALID_USERNAME, VALID_PASSWORD,
    PRODUCT_NAME, PRODUCT_PRICE,
    CART_PAGE_TITLE
)

#------------Smoke Test----------

@pytest.mark.smoke
@pytest.mark.cart
def test_cart_page_loads( login_page, home_page, cart_page):
    """Test cart page open loads correctly"""
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    home_page.go_to_cart()
    assert cart_page.is_cart_page_loaded(), \
        "Cart page did not load"

@pytest.mark.smoke
@pytest.mark.cart
def test_add_item_to_cart( login_page, home_page, cart_page):
    """Test item added from home appears in cart."""
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    home_page.add_product_by_name(PRODUCT_NAME)
    home_page.go_to_cart()
    assert cart_page.is_item_in_cart(PRODUCT_NAME), \
        f"{PRODUCT_NAME} was not added to cart"

#------------ Regression Test-------------

@pytest.mark.regression
@pytest.mark.cart
def test_cart_item_count( login_page, home_page, cart_page):
    """Test cart shows correct item count."""
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    home_page.add_product_by_name(PRODUCT_NAME)
    home_page.go_to_cart()
    assert cart_page.get_cart_item_count() == 1, \
        "Cart item count is not 1"

@pytest.mark.regression
@pytest.mark.cart
def test_cart_item_price( login_page, home_page, cart_page):
    """Test cart shows correct item price."""
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    home_page.add_product_by_name(PRODUCT_NAME)
    home_page.go_to_cart()
    price = cart_page.get_cart_item_prices()

    assert PRODUCT_PRICE in price, \
        f"Expected price {PRODUCT_PRICE} was not found in cart"

@pytest.mark.regression
@pytest.mark.cart
def test_remove_item_from_cart( login_page, home_page, cart_page):
    """Test removing item from cart makes cart empty"""
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    home_page.add_product_by_name(PRODUCT_NAME)
    home_page.go_to_cart()
    cart_page.remove_item_from_cart()
    assert cart_page.is_cart_empty(), \
        "Cart is not empty after removing item"

@pytest.mark.regression
@pytest.mark.cart
def test_continue_shopping( login_page, home_page, cart_page):
    """Test continue shopping returns to home page"""
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    home_page.go_to_cart()
    cart_page.continue_shopping()
    assert home_page.is_home_page_loaded(), \
        "did not return to home page after continue shopping"

@pytest.mark.regression
@pytest.mark.cart
def test_proceed_to_checkout( login_page, home_page, cart_page):
    """Test checkout button navigates to checkout page"""
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    home_page.add_product_by_name(PRODUCT_NAME)
    home_page.go_to_cart()
    cart_page.proceed_to_checkout()
    assert "checkout" in cart_page.get_current_url(), \
        "Did not navigate to checkout page"