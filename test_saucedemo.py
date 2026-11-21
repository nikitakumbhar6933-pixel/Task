import os
import re
import pytest
from tests.conftest import login

pytestmark = pytest.mark.ui
PASSWORD = os.getenv("SAUCE_PASSWORD", "secret_sauce")

def test_01_standard_user_login(browser_page):
    login(browser_page)
    assert browser_page.url.endswith("/inventory.html")
    assert browser_page.locator('[data-test="title"]').inner_text() == "Products"

def test_02_locked_out_user_login(browser_page):
    login(browser_page, "locked_out_user", PASSWORD)
    error = browser_page.locator('[data-test="error"]')
    assert error.is_visible()
    assert "locked out" in error.inner_text().lower()

def test_03_invalid_password_login(browser_page):
    login(browser_page, "standard_user", "wrong_password")
    assert browser_page.locator('[data-test="error"]').is_visible()
    assert browser_page.url.endswith("/")

def test_04_sort_products_name_descending(browser_page):
    login(browser_page)
    browser_page.locator('[data-test="product-sort-container"]').select_option("za")
    names = browser_page.locator('[data-test="inventory-item-name"]').all_inner_texts()
    assert names == sorted(names, reverse=True)

def test_05_add_product_to_cart(browser_page):
    login(browser_page)
    browser_page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    assert browser_page.locator('[data-test="shopping-cart-badge"]').inner_text() == "1"
    assert browser_page.locator('[data-test="remove-sauce-labs-backpack"]').is_visible()

def test_06_remove_product_from_cart(browser_page):
    login(browser_page)
    browser_page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    browser_page.locator('[data-test="remove-sauce-labs-backpack"]').click()
    assert browser_page.locator('[data-test="shopping-cart-badge"]').count() == 0

def test_07_checkout_required_field_validation(browser_page):
    login(browser_page)
    browser_page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    browser_page.locator('[data-test="shopping-cart-link"]').click()
    browser_page.locator('[data-test="checkout"]').click()
    browser_page.locator('[data-test="continue"]').click()
    assert "first name" in browser_page.locator('[data-test="error"]').inner_text().lower()

def test_08_complete_purchase_flow(browser_page):
    login(browser_page)
    browser_page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    browser_page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click()
    browser_page.locator('[data-test="shopping-cart-link"]').click()
    assert browser_page.locator('[data-test="cart-item"]').count() == 2
    browser_page.locator('[data-test="checkout"]').click()
    browser_page.locator('[data-test="firstName"]').fill("QA")
    browser_page.locator('[data-test="lastName"]').fill("Tester")
    browser_page.locator('[data-test="postalCode"]').fill("400001")
    browser_page.locator('[data-test="continue"]').click()
    assert browser_page.locator('[data-test="checkout_summary_container"]').is_visible()
    browser_page.locator('[data-test="finish"]').click()
    assert "Thank you for your order" in browser_page.locator('[data-test="complete-header"]').inner_text()

def test_09_problem_user_capture_inventory_evidence(browser_page):
    login(browser_page, "problem_user", PASSWORD)
    browser_page.screenshot(path="evidence/problem-user-inventory.png", full_page=True)
    images = browser_page.locator('[data-test="inventory-item"] img').evaluate_all(
        "(imgs) => imgs.map(i => ({src: i.getAttribute('src'), complete: i.complete, width: i.naturalWidth}))"
    )
    # Diagnostic evidence only: do not fail the full suite on intentionally seeded visual defects.
    assert len(images) > 0
