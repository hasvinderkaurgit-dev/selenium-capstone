from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

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

    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    def apply_filter(self, option_text):
        dropdown = Select(self.driver.find_element(*self.SORT_DROPDOWN))
        dropdown.select_by_visible_text(option_text)
        return self

    def get_item_names(self):
        elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [el.text for el in elements]

    def get_item_prices(self):
        elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        return [float(el.text.replace("$", "")) for el in elements]

    