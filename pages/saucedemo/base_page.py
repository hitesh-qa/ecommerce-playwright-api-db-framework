from playwright.sync_api import Page


class BasePage:
    """Base class for all page objects."""

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def get_current_url(self):
        return self.page.url

    def get_title(self):
        return self.page.title()

    def click(self, locator: str):
        self.page.locator(locator).click()

    def fill(self, locator: str, text: str):
        self.page.locator(locator).fill(text)

    def get_text(self, locator: str):
        return self.page.locator(locator).text_content()

    def is_visible(self, locator: str):
        return self.page.locator(locator).is_visible()

    def wait_for_element(self, locator: str):
        self.page.locator(locator).wait_for(state="visible")

    def wait_for_url(self, url: str):
        self.page.wait_for_url(url)

    def take_screenshot(self, name: str):
        self.page.screenshot(path=f"screenshots/{name}.png")