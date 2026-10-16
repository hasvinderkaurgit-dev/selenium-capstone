from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class CartPage(BasePage):
    URL = "https://www.saucedemo.com/cart.html"
    CART_CONTAINER = (By.ID, "shopping_cart_container")
    CART_LINK = (By.CSS_SELECTOR, "a[data-test='shopping-cart-link']")
    CART_BADGE = (By.CSS_SELECTOR, "span[data-test='shopping-cart-badge']")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    PAGE_TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    SORT_DROPDOWN = (By.CSS_SELECTOR, "[data-test='product-sort-container']")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def open_cart(self):
        self._click(self.CART_LINK)
        self.wait.until(EC.visibility_of_element_located(self.PAGE_TITLE))
        return self

    def click_checkout(self):
        self._click(self.CHECKOUT_BUTTON)
        return self

    def get_item_count(self):
        """Return the number shown in the cart badge."""
        badge = self.driver.find_elements(*self.CART_BADGE)
        return int(badge[0].text) if badge else 0

    def is_cart_visible(self):
        """Check if the cart container is displayed."""
        return self.driver.find_element(*self.CART_CONTAINER).is_displayed()

    def get_cart_items(self):
        """Return a list of item names in the cart."""
        elements = self.driver.find_elements(*self.ITEM_NAME)
        return [el.text for el in elements]

    def wait_for_items(self, expected_items):
        """Wait until the cart contents match the expected item names."""
        def items_match(_):
            try:
                return sorted(self.get_cart_items()) == sorted(expected_items)
            except StaleElementReferenceException:
                return False

        self.wait.until(items_match)
        return self

    def apply_filter(self, option_text):
        """Apply a filter from the sort dropdown."""
        dropdown = self.driver.find_element(*self.SORT_DROPDOWN)
        for option in dropdown.find_elements(By.TAG_NAME, "option"):
            if option.text == option_text:
                option.click()
                break
        return self