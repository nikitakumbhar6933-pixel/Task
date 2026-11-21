import os
import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://www.saucedemo.com/"
USERNAME = os.getenv("SAUCE_USERNAME", "standard_user")
PASSWORD = os.getenv("SAUCE_PASSWORD", "secret_sauce")

@pytest.fixture
def browser_page():
    headless = os.getenv("HEADLESS", "true").lower() != "false"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        page = browser.new_page(viewport={"width": 1366, "height": 768})
        page.goto(BASE_URL, wait_until="domcontentloaded")
        yield page
        browser.close()

def login(page, username=USERNAME, password=PASSWORD):
    page.locator('[data-test="username"]').fill(username)
    page.locator('[data-test="password"]').fill(password)
    page.locator('[data-test="login-button"]').click()
