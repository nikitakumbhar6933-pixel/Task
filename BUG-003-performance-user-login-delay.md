# BUG-003 — Login delay for `performance_glitch_user`

- **Area:** Login / Performance
- **Severity:** Medium
- **Priority:** High
- **Status:** Draft — measure and attach evidence before filing
- **Test account:** `performance_glitch_user` / `secret_sauce`

## Steps to reproduce
1. Open https://www.saucedemo.com/.
2. Start a timer immediately before clicking Login.
3. Enter `performance_glitch_user` and `secret_sauce`.
4. Click Login and stop the timer when the Products inventory is usable.
5. Repeat at least three times under a stable network and record each duration.

## Expected result
The user is authenticated and the inventory page becomes usable within the agreed performance threshold. For this assessment, use 3 seconds as a proposed target, not a published product SLA.

## Actual result
This seeded persona is intended to exercise slow-login behavior. Public test examples report a noticeable delay, but the measured duration must be captured in this test environment. Record actual seconds and do not copy another tester's measurement.

## Evidence
Attach a screenshot of the loaded inventory page and a timing record (three trials, browser version, OS, network conditions).
