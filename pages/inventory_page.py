from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class InventoryPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"

    def load(self):
        self.driver.get(self.URL)
        return self

    def is_loaded(self):
        return "inventory.html" in self.driver.current_url

    def add_to_cart(self, product_id):
        add_locator = (By.ID, f"add-to-cart-{product_id}")
        remove_locator = (By.ID, f"remove-{product_id}")
        self._click(add_locator)
        self.wait.until(EC.presence_of_element_located(remove_locator))
        return self

    def remove_from_cart(self, product_id):
        remove_locator = (By.ID, f"remove-{product_id}")
        add_locator = (By.ID, f"add-to-cart-{product_id}")
        self._click(remove_locator)
        self.wait.until(EC.presence_of_element_located(add_locator))
        return self

    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    def apply_filter(self, option_text):
        """Apply a filter from the sort dropdown."""
        dropdown = self.driver.find_element(*self.SORT_DROPDOWN)
        for option in dropdown.find_elements(By.TAG_NAME, "option"):
            if option.text == option_text:
                option.click()
                break
        return self

    def get_item_names(self):
        elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [el.text for el in elements]

    def get_item_prices(self):
        elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        return [float(el.text.replace("$", "")) for el in elements]

    