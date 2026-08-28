

class ConfirmationPage:
    def __init__(self, page):
        self.page = page

    def get_order_id(self) -> int:
        text = self.page.locator("#order-id").inner_text()
        return int(text.replace("order #", "").strip())

    def get_status(self) -> int:
        text = self.page.locator("#order-status").inner_text()
        return text.replace("Status:", "").strip()

    def get_total(self) -> float:
        text = self.page.locator("#order-total").inner_text()
        return float(text.replace("Total: $", "").strip())
