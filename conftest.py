import pytest
from pytest_html import extras
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    chromedriver_path = os.environ.get("CHROMEDRIVER_PATH")
    service = Service(chromedriver_path) if chromedriver_path else Service()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:  ## only caputures failures
    #if report.when == "call" --- to capture screenshots for all test cases, not just failed ones  
        driver = item.funcargs.get("driver")
        if driver:
            screenshot_b64 = driver.get_screenshot_as_base64()
            extra.append(extras.image(screenshot_b64, mime_type="image/png"))

    report.extras = extra