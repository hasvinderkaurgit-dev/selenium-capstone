from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"


    def is_loaded(self):
        return "inventory.html" in self.driver.current_url

    def add_to_cart(self, product_id):
        self._click((By.ID, f"add-to-cart-{product_id}"))
        return self

    def remove_from_cart(self, product_id):
        locator = (By.ID, f"remove-{product_id}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        return self