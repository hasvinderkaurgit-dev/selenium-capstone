from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.inventory_page import InventoryPage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    ERROR_BUTTON = (By.CSS_SELECTOR, "button[data-test='error-button']")

    def load(self):
        self.driver.get(self.URL)
        return self

    def login(self, username, password):
        self._type(self.USERNAME_INPUT, username)
        self._type(self.PASSWORD_INPUT, password)
        self._click(self.SUBMIT_BUTTON)
        self.wait.until(
        lambda d: "inventory.html" in d.current_url or self._is_error_visible()
        )
        if "inventory.html" in self.driver.current_url:
            return InventoryPage(self.driver)
        return self

    def _is_error_visible(self):
        elements = self.driver.find_elements(*self.ERROR_MESSAGE)
        return bool(elements) and elements[0].is_displayed()

    def get_error_message(self):
        return self._find(self.ERROR_MESSAGE).text

    def is_logged_in(self):
        return "inventory.html" in self.driver.current_url

    
