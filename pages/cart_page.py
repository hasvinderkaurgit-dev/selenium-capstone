from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ShoppingCart(BasePage):
    URL = "https://www.saucedemo.com/cart.html"
    CART_CONTAINER = (By.ID, "shopping_cart_container")
    CART_LINK = (By.CSS_SELECTOR, "a[data-test='shopping-cart-link']")
    CART_BADGE = (By.CSS_SELECTOR, "span[data-test='shopping-cart-badge']")

    def open_cart(self):
        """Click the shopping cart link to open the cart."""
        self.driver.find_element(*self.CART_LINK).click()

    def get_item_count(self):
        """Return the number shown in the cart badge."""
        badge = self.driver.find_elements(*self.CART_BADGE)
        return int(badge[0].text) if badge else 0

    def is_cart_visible(self):
        """Check if the cart container is displayed."""
        return self.driver.find_element(*self.CART_CONTAINER).is_displayed()