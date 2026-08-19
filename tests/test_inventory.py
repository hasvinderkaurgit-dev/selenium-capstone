import pytest
from conftest import driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


#def test_login(driver):
#    inventory_page = LoginPage(driver).load().login("standard_user", "secret_sauce")
#    assert inventory_page.is_loaded()

@pytest.mark.parametrize("selected_items", [
    ["sauce-labs-backpack"],                       # single item
    ["sauce-labs-backpack", "sauce-labs-bike-light"],         # two items
    ["sauce-labs-backpack", "sauce-labs-bike-light", "sauce-labs-bolt-t-shirt"], # three items
    ["sauce-labs-onesie", "sauce-labs-fleece-jacket"], # different combo
])
def test_add_items(driver, selected_items):

    inventory = LoginPage(driver).load().login("standard_user", "secret_sauce")
    cart = CartPage(driver)

    # Ensure inventory page is loaded
    assert inventory.is_loaded()

    # Add items dynamically
    for item in selected_items:
        inventory.add_to_cart(item)

    # Assert badge count matches number of items added
    assert cart.get_item_count() == len(selected_items)

    # Remove items
    for item in selected_items:
        inventory.remove_from_cart(item)

    #Verify badge count after removing
    assert cart.get_item_count() == 0