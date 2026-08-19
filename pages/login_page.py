from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    ERROR_BUTTON = (By.CSS_SELECTOR, "button[data-test='error-button']")

    def load(self):
        self.driver.get(self.URL)
        return self

    def login(self, username, password):
        self._type(self.USERNAME_INPUT, username)
        self._type(self.PASSWORD_INPUT, password)
        self._click(self.SUBMIT_BUTTON)
        return self

    def get_error_message(self):
        return self._find(self.ERROR_MESSAGE).text

    def is_logged_in(self):
        return "inventory.html" in self.driver.current_url

    
