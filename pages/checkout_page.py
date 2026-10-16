from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    URL = "https://www.saucedemo.com/checkout-step-one.html"

    PAGE_TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    FINISH_BUTTON = (By.ID, "finish")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    COMPLETE_HEADER = (By.CSS_SELECTOR, "[data-test='complete-header']")


    def load(self):
         self.driver.get(self.URL)
         return self

    def get_page_title(self):
        return self._find(self.PAGE_TITLE).text


    def fill_checkout_info(self, first_name, last_name, zip_code):
        self._type(self.FIRST_NAME, first_name)
        self._type(self.LAST_NAME, last_name)
        self._type(self.ZIP_CODE, zip_code)
        return self

    def click_continue(self):
        self._click(self.CONTINUE_BUTTON)
        return self
    
    def click_finish(self):
        self._click(self.FINISH_BUTTON)
        return self

    def get_completion_message(self):
        return self._find(self.COMPLETE_HEADER).text

    def get_error_message(self):
        return self._find(self.ERROR_MESSAGE).text