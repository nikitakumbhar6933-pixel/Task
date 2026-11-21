# BUG-001 — Product image mismatch for `problem_user`

- **Area:** Product listing / UI
- **Severity:** Medium
- **Priority:** Medium
- **Status:** Draft — reproduce and attach evidence before filing
- **Test account:** `problem_user` / `secret_sauce`

## Preconditions
Open https://www.saucedemo.com/ in a supported desktop browser.

## Steps to reproduce
1. Sign in as `problem_user`.
2. Wait for the inventory page to load.
3. Compare each product thumbnail with the corresponding product name and product detail image.
4. Capture the inventory and detail-page screenshots.

## Expected result
Each inventory product displays its own matching product image, and the image remains consistent on its detail page.

## Actual result
Known seeded-user behavior reported for this persona: product imagery may be mismatched relative to the product name. **Confirm the exact affected item(s) and observed result during execution; do not file until reproduced.**

## Evidence
Attach `evidence/problem-user-inventory.png` after running:
```bash
pytest tests/ui/test_saucedemo.py::test_09_problem_user_capture_inventory_evidence -v
```
Record browser version, OS, date/time and exact product(s) affected.
