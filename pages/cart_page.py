from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    URL = "https://www.saucedemo.com/cart.html"

    CART_LINK = (By.CSS_SELECTOR, "a[data-test='shopping-cart-link']")
    CART_BADGE = (By.CSS_SELECTOR, "span[data-test='shopping-cart-badge']")

    def open(self):
        self._click(self.CART_LINK)
        return self

    def get_item_count(self):
        badges = self.driver.find_elements(*self.CART_BADGE)
        return int(badges[0].text) if badges else 0