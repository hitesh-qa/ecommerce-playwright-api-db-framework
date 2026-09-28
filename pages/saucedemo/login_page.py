from pages.saucedemo.base_page import BasePage
from test_data.data import BASE_URL


class LoginPage(BasePage):
    """Page object for the Login page."""

    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def open(self):
        self.navigate(BASE_URL)

    def enter_username(self, username: str):
        self.fill(self.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        self.fill(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_visible(self):
        return self.is_visible(self.ERROR_MESSAGE)

    def is_login_successful(self):
        return "inventory" in self.get_current_url()