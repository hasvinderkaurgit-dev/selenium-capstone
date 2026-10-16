import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username,password,expected_url,expected_error", [
    ("standard_user", "secret_sauce", "https://www.saucedemo.com/inventory.html", None),
    ("problem_user", "secret_sauce", "https://www.saucedemo.com/inventory.html", None),
    ("performance_glitch_user", "secret_sauce", "https://www.saucedemo.com/inventory.html", None),
    ("error_user", "secret_sauce", "https://www.saucedemo.com/inventory.html", None),
    ("visual_user", "secret_sauce", "https://www.saucedemo.com/inventory.html", None),
    ("locked_out_user", "secret_sauce", "https://www.saucedemo.com/", "Epic sadface: Sorry, this user has been locked out."),
    ("wronguser", "wrongpass", "https://www.saucedemo.com/", "Epic sadface: Username and password do not match any user in this service")
])
def test_login(driver, username, password, expected_url, expected_error):
    page = LoginPage(driver).load().login(username, password)
    assert expected_url in page.driver.current_url
    if expected_error:
        assert expected_error in page.get_error_message()
