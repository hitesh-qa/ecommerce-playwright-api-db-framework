
from pages.saucedemo.base_page import BasePage

class ProductPage(BasePage):
    """Page object for the Product Detail page."""

#--------------Locators----------
PRODUCT_NAME = ".inventory_details_name"
PRODUCT_PRICE = ".inventory_details_price"
PRODUCT_DESC = ".inventory_details_desc"
PRODUCT_IMAGE = ".inventory_details_img"
ADD_TO_CART_BUTTON = "button[data-test^='add-to-cart']"
REMOVE_BUTTON = "button[data-test^='remove']"
BACK_BUTTON = "#back-to-products"

#------------Actions-------------
def get_product_name(self):
    """Return product name text."""
    return self.get_text(self.PRODUCT_NAME)

def get_product_price(self):
    """Return product price text."""
    return self.get_text(self.PRODUCT_PRICE)

def get_product_description(self):
    """Return product description text."""
    return self.get_text(self.PRODUCT_DESC)

def add_to_cart(self):
    """Click Add to cart button."""
    self.click(self.ADD_TO_CART_BUTTON)

def remove_from_cart(self):
    """Click Remove button."""
    self.click(self.REMOVE_BUTTON)

def go_back(self):
    """Click back to products button."""
    self.click(self.BACK_BUTTON)

#-------------Assertions---------

def is_product_page_loaded(self):
    """Check if product page is loaded."""
    return self.is_visible(self.PRODUCT_NAME)

def is_add_to_cart_visible(self):
    """Check if Add to Cart button is visible."""
    return self.is_visible(self.ADD_TO_CART_BUTTON)

def is_remove_button_visible(self):
    """Check if remove button is visible after adding."""
    return self.is_visible(self.REMOVE_BUTTON)