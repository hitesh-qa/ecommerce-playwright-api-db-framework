


class ProductPage:
    URL = "http://127.0.0.1:5000/"

    def __init__(self, page):
        self.page = page

    def goto(self):
        self.page.goto(self.URL)

    def buy_product(self, product_id: int, quantity: int = 1):
        form = self.page.locator(f"form:has(input[name='product_id'][value='{product_id}'])")
        form.locator("input[name='quantity']").fill(str(quantity))
        form.locator("button[type='submit']").click()