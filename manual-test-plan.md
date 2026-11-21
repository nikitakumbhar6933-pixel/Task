# Manual Test Plan — SauceDemo

## 1. Objective
Validate core customer journeys and key negative/edge conditions for login, product listing and sorting, cart management, and checkout on SauceDemo.

## 2. Scope
**In scope:** login, authentication errors, product inventory, product sorting, add/remove cart, cart contents, checkout form validation, order overview, order completion, seeded-user behavior.

**Out of scope:** payment gateway integration, backend/database verification, security penetration testing, load testing beyond observing the seeded performance persona, and production payment processing.

## 3. Test environment
- Application: https://www.saucedemo.com/
- Browser: Chromium (Playwright); manually record exact browser version
- OS: record actual OS/version at execution
- Viewports: desktop 1366×768 and mobile emulation 390×844
- Test data: seeded accounts; password `secret_sauce`
- Normal flow account: `standard_user`
- Negative account: `locked_out_user`
- Diagnostic accounts: `problem_user`, `performance_glitch_user`

## 4. Entry criteria
- Target site is reachable.
- Browser and test dependencies are installed.
- Test credentials are available.
- No active outage is known.

## 5. Exit criteria
- All planned cases have Pass/Fail/Blocked status and evidence.
- Critical/high defects are reported.
- No unresolved blocker prevents the standard purchase journey.
- Automated tests complete and results are reviewed.

## 6. Approach
1. Execute smoke tests for login and product inventory.
2. Execute functional tests for sorting and cart behavior.
3. Execute checkout validation and end-to-end purchase.
4. Execute negative and boundary cases.
5. Compare seeded-user behavior and capture screenshots for confirmed anomalies.
6. Run automated regression and API tests.

## 7. Risks and mitigations
- **Seeded-user defects are intentional:** distinguish expected demo behavior from product defects; report only after reproducible observation.
- **Network latency:** record timestamps and rerun performance observations.
- **External API rate limits or authentication changes:** record response and configure `REQRES_API_KEY` if required.
- **Dynamic inventory order:** assert sort order against actual displayed names rather than hard-coded item positions.

## 8. Deliverables
- `test-cases.csv` — 30 manual test cases.
- `tests/ui/` — Playwright UI automation.
- `tests/api/` — ReqRes API tests.
- `bug-reports/` — three reproduction-ready issue drafts.
- `evidence/` — screenshots captured during execution.
