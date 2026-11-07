import pytest
from pages.saucedemo.login_page import LoginPage
from test_data.data import BASE_URL
from pages.saucedemo.home_page import HomePage
from pages.saucedemo.product_page import ProductPage
from pages.saucedemo.cart_page import CartPage

@pytest.fixture(scope="function")
def login_page(page):
    page.goto(BASE_URL)
    return LoginPage(page)

@pytest.fixture(scope="function")
def home_page(page):
    return HomePage(page)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)

@pytest.fixture(scope="function")
def product_page(page):
    return ProductPage(page)


@pytest.fixture(scope="function")
def cart_page(page):
    return CartPage(page)