# SauceDemo Test Automation Suite

Automated UI test suite for [saucedemo.com](https://www.saucedemo.com/), built with Python, Selenium WebDriver, and pytest. Covers login, inventory/cart management, and the checkout flow using the Page Object Model (POM) design pattern.

## Tech Stack

- **Python 3.10+**
- **Selenium 4** — browser automation
- **pytest** — test runner, fixtures, parametrization
- **pytest-html** — HTML test reports with embedded failure screenshots
- **pytest-rerunfailures** — automatic retry of flaky test failures
- **GitHub Actions** — CI pipeline, runs the full suite headless on every push

## Project Structure

```
selenium-capstone/
├── conftest.py              # Shared fixtures (driver, wait) and screenshot-on-failure hook
├── pytest.ini               # pytest config (paths, report generation, rerun settings)
├── requirements.txt         # Pinned dependencies
├── pages/                   # Page Object Model classes
│   ├── base_page.py         # Shared wait-safe find/click/type helpers
│   ├── login_page.py        # Login page + credential validation
│   ├── inventory_page.py    # Product listing, add/remove cart, sorting
│   ├── cart_page.py         # Cart contents and checkout trigger
│   └── checkout_page.py     # Multi-step checkout flow
├── tests/
│   ├── test_login.py        # Valid/invalid login scenarios
│   ├── test_inventory.py    # Add/remove cart items, sorting
│   └── test_checkout.py     # Happy-path checkout + form validation errors
└── .github/workflows/
    └── tests.yml            # CI pipeline definition
```

## Setup

1. Clone the repository and create a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. **ChromeDriver:** Selenium's built-in Selenium Manager handles this automatically on most platforms. If you're on an architecture it doesn't support (e.g. Windows ARM64), download a matching [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/) build manually and set:
   ```
   setx CHROMEDRIVER_PATH "C:\path\to\chromedriver.exe"
   ```
   The test fixture in `conftest.py` checks for this environment variable and falls back to Selenium Manager if it isn't set.

## Running the Tests

Run the full suite:
```
pytest -v
```

Run a specific file or test:
```
pytest -v tests/test_login.py
pytest -v -k "locked_out_user"
```

Each run generates `report.html` (self-contained, includes embedded screenshots for any failures) alongside the console output, thanks to settings in `pytest.ini`.

## Test Coverage

- **Login** (`test_login.py`) — parametrized across all SauceDemo demo accounts (standard, problem, performance-glitch, error, visual, locked-out) plus invalid credentials; verifies correct redirect or correct error message for each.
- **Inventory & Cart** (`test_inventory.py`) — adding/removing single and multiple items, verifying cart badge counts and actual cart contents stay in sync through partial add/remove sequences; product sort/filter verification (by name and price).
- **Checkout** (`test_checkout.py`) — full happy path from cart through order confirmation, plus negative cases for each required field (first name, last name, postal code) left blank.

## CI/CD

Every push to `main` triggers the GitHub Actions workflow (`.github/workflows/tests.yml`), which installs dependencies, runs the suite headless on a standard Linux runner, and uploads `report.html` as a downloadable artifact — viewable from the run's summary page in the **Actions** tab, regardless of pass or fail.

## Design Notes

- All page interactions go through `BasePage`'s wait-safe helpers (`_find`, `_click`, `_type`) rather than raw Selenium calls, so every action waits for its target element to be genuinely ready before proceeding.
- `LoginPage.login()` returns either an `InventoryPage` (on success) or `self` (on failure), so tests can chain directly into whichever page object matches the actual outcome.
- Flaky failures (occasional slow responses from the external demo site) are mitigated with `pytest-rerunfailures`, configured via `addopts` in `pytest.ini`.