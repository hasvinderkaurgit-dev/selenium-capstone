import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_success(driver):
    inventory = LoginPage(driver).load().login("standard_user", "secret_sauce")
    inventory.add_to_cart("sauce-labs-backpack")
    cart = CartPage(driver)
    cart.open_cart()
    cart.click_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_checkout_info("Taylor", "Tester", "12345")
    checkout.click_continue()
    checkout.click_finish()

    assert checkout.get_completion_message() == "Thank you for your order!"



@pytest.mark.parametrize("first_name,last_name,postcode,error_message", [
    ("Taylor", "", "12345", "Error: Last Name is required"),
    ("", "Tester", "12345", "Error: First Name is required"),
    ("", "", "", "Error: First Name is required"),
    ("Taylor", "Tester", "", "Error: Postal Code is required")
])

def test_checkout_fail(driver, first_name, last_name, postcode, error_message):
    inventory = LoginPage(driver).load().login("standard_user", "secret_sauce")
    inventory.add_to_cart("sauce-labs-backpack")
    cart = CartPage(driver)
    cart.open_cart()
    cart.click_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_checkout_info(first_name, last_name, postcode)
    checkout.click_continue()

    assert checkout.get_error_message() == error_message