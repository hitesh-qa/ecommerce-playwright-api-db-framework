import pytest
from test_data.data import(
VALID_USERNAME, VALID_PASSWORD,
INVALID_USERNAME, INVALID_PASSWORD,
LOCKED_USER,LOGIN_ERROR_MSG, LOCKED_ERROR_MSG
)

#------------Smoke Tests----------------
@pytest.mark.smoke
@pytest.mark.login
def test_valid_login( login_page):
    """Test login with valid credentials."""
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    assert login_page.is_login_successful(), \
    "Login failed - inventory page not loaded"

@pytest.mark.smoke
@pytest.mark.login
def test_invalid_login( login_page):
    """Test login with invalid credentials shows error."""
    login_page.open()
    login_page.login(INVALID_USERNAME, INVALID_PASSWORD)
    assert login_page.is_error_visible(), \
        "Error message not displayed"
    assert LOGIN_ERROR_MSG in login_page.get_error_message(), \
        "Wrong error message displayed"

#--------------Regression Tests---------------

@pytest.mark.regression
@pytest.mark.login
def test_locked_out_user( login_page):
    """Test locked out user sees correct error."""
    login_page.open()
    login_page.login(LOCKED_USER, VALID_PASSWORD)
    assert login_page.is_error_visible(), \
        "Error message not displayed for locked user."
    assert LOCKED_ERROR_MSG in login_page.get_error_message(), \
        "Wrong error message for locked user."

@pytest.mark.regression
@pytest.mark.login
def test_empty_username( login_page):
    """Test login with empty username shows error."""
    login_page.open()
    login_page.login("", INVALID_PASSWORD)
    assert login_page.is_error_visible(), \
    "Error message not displayed for empty username."

@pytest.mark.regression
@pytest.mark.login
def test_empty_password( login_page):
    """Test login with empty password shows error."""
    login_page.open()
    login_page.login( INVALID_USERNAME, "")
    assert login_page.is_error_visible(), \
    "Error message not displayed for empty password."

@pytest.mark.regression
@pytest.mark.login
def test_empty_both_fields(login_page):
    """Test login with both fields empty shows error."""
    login_page.open()
    login_page.login( "", "")
    assert login_page.is_error_visible(), \
    "Error message not displayed for empty username."