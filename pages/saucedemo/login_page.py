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

