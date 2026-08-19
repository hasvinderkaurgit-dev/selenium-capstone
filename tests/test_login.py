import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username,password,expected_url", [
    ("standard_user", "secret_sauce", "https://www.saucedemo.com/inventory.html"),
    ("problem_user", "secret_sauce", "https://www.saucedemo.com/inventory.html"),
    ("performance_glitch_user", "secret_sauce", "https://www.saucedemo.com/inventory.html"),
    ("error_user", "secret_sauce", "https://www.saucedemo.com/inventory.html"),
    ("visual_user", "secret_sauce", "https://www.saucedemo.com/inventory.html"),
    ("locked_out_user", "secret_sauce", "https://www.saucedemo.com/"),
    ("wronguser", "wrongpass", "https://www.saucedemo.com/"),
    
])
def test_login(driver, username, password, expected_url):
    login_page = LoginPage(driver).load().login(username, password)
    assert expected_url in login_page.driver.current_url

def locked_user(driver,username,password):
    login_page = LoginPage(driver).load().login(username, password)
    assert "Epic sadface: Sorry, this user has been locked out." in login_page.get_error_message()

def wrong_user(driver,username,password):
    login_page = LoginPage(driver).load().login(username, password)
    assert "Epic sadface: Username and password do not match any user in this service" in login_page.get_error_message()