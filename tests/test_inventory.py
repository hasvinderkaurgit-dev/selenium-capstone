import pytest
from conftest import driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


#def test_login(driver):
#    inventory_page = LoginPage(driver).load().login("standard_user", "secret_sauce")
#    assert inventory_page.is_loaded()

#@pytest.mark.parametrize("selected_items", [
#    ["sauce-labs-backpack"],                       # single item
#    ["sauce-labs-backpack", "sauce-labs-bike-light"],         # two items
#    ["sauce-labs-backpack", "sauce-labs-bike-light", "sauce-labs-bolt-t-shirt"], # three items
#    ["sauce-labs-onesie", "sauce-labs-fleece-jacket"], # different combo
#])
#def test_add_items(driver, selected_items):

#    inventory = LoginPage(driver).load().login("standard_user", "secret_sauce")
#    cart = CartPage(driver)

#    # Ensure inventory page is loaded
#    assert inventory.is_loaded()

#    # Add items dynamically
#    for item in selected_items:
#        inventory.add_to_cart(item)

#    # Assert badge count matches number of items added
#    assert cart.get_item_count() == len(selected_items)

#    # Remove items
#    for item in selected_items:
#        inventory.remove_from_cart(item)
#
#    #Verify badge count after removing
#    assert cart.get_item_count() == 0


@pytest.mark.parametrize("selected_items, items_to_remove", [
    (["sauce-labs-backpack"], ["sauce-labs-backpack"]),  # add 1, remove 1
    (["sauce-labs-backpack", "sauce-labs-bike-light"], ["sauce-labs-backpack"]),  # add 2, remove 1
    (["sauce-labs-backpack", "sauce-labs-bike-light", "sauce-labs-bolt-t-shirt"], ["sauce-labs-bike-light", "sauce-labs-bolt-t-shirt"]),  # add 3, remove 2
    (["sauce-labs-onesie", "sauce-labs-fleece-jacket"], ["sauce-labs-onesie"]),  # add 2, remove 1
])
def test_add_and_partial_remove(driver, selected_items, items_to_remove):
    inventory = LoginPage(driver).load().login("standard_user", "secret_sauce")
    cart = CartPage(driver)

    # Step 1: Add all items
    for item in selected_items:
        inventory.add_to_cart(item)
    assert cart.get_item_count() == len(selected_items)

    # Step 2: Remove only the specified subset
    for item in items_to_remove:
        inventory.remove_from_cart(item)

    # Step 3: Verify badge count reflects remaining items
    expected_count = len(selected_items) - len(items_to_remove)
    assert cart.get_item_count() == expected_count

    # Step 4: Clean up — remove the rest so cart is empty
    remaining_items = [i for i in selected_items if i not in items_to_remove]
    for item in remaining_items:
        inventory.remove_from_cart(item)
    assert cart.get_item_count() == 0
