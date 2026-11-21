# BUG-002 — Cart action behaves inconsistently for `problem_user`

- **Area:** Product listing / Cart
- **Severity:** High (if a selected product cannot be added or removed)
- **Priority:** High (if purchase completion is blocked)
- **Status:** Draft — reproduce and attach evidence before filing
- **Test account:** `problem_user` / `secret_sauce`

## Steps to reproduce
1. Sign in as `problem_user`.
2. On the inventory page, click **Add to cart** for each product individually.
3. Verify the button changes to **Remove** and the cart badge increments.
4. Open the cart and compare its contents with the selected products.
5. Repeat for any product that did not behave as expected.

## Expected result
Every available product can be added and removed; the cart badge and cart contents stay synchronized with the user's actions.

## Actual result
The `problem_user` persona is a seeded diagnostic account associated with inconsistent product/cart interactions in test examples. **The exact failing product and actual UI response must be observed and recorded during this run.** This draft is not an independently verified finding.

## Evidence
Attach screenshots showing the product button state, cart badge, and cart contents. Record the product name and whether the cart count/content changed.
