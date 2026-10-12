from pages.saucedemo.base_page import BasePage

class HomePage(BasePage):
    """Page object for the Home/Inventory page."""

    PAGE_TITLE = ".title"
    PRODUCT_LIST = ".inventory_list"
    PRODUCT_ITEMS = ".inventory_item"
    PRODUCT_NAMES = ".inventory_item_name"
    PRODUCT_PRICES = ".inventory_item_price"
    ADD_TO_CART_BUTTON = "button[data-test^='add-to-cart']"
    CART_ICON = ".shopping_cart_link"
    CART_BADGE = ".shopping_cart_badge"
    SORT_DROPDOWN = ".product_sort_container"
    BURGER_MENU = "#react-burger-menu-btn"
    LOGOUT_LINK = "#logout_sidebar_link"

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def get_all_product_names(self):
        return self.page.locator(self.PRODUCT_NAMES).all_text_contents()

    def get_all_product_prices(self):
        return self.page.locator(self.PRODUCT_PRICES).all_text_contents()

    def add_first_product_to_cart(self):
        self.page.locator(self.ADD_TO_CART_BUTTON).first.click()

    def add_product_by_name(self, product_name: str):
        self.page.locator(
            f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
        ).click()

    def get_cart_count(self):
        if self.is_visible(self.CART_BADGE):
            return self.get_text(self.CART_BADGE)
        return "0"

    def go_to_cart(self):
        self.click(self.CART_ICON)

    def sort_products(self, option: str):
        self.page.locator(self.SORT_DROPDOWN).select_option(option)

    def logout(self):
        self.click(self.BURGER_MENU)
        self.page.wait_for_selector(self.LOGOUT_LINK)
        self.click(self.LOGOUT_LINK)

    def is_home_page_loaded(self):
        return self.is_visible(self.PRODUCT_LIST)

    def is_cart_badge_visible(self):
        return self.is_visible(self.CART_BADGE)