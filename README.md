# SauceDemo QA Assessment — Python + Playwright + Pytest

A repo-ready QA portfolio project covering manual test design, UI automation, API automation, and bug-report drafts.

## Scope
- UI under test: https://www.saucedemo.com/
- API under test: https://reqres.in/
- UI stack: Python, Playwright, pytest
- API stack: Python Requests, pytest

## Prerequisites
- Python 3.10+
- Internet access to the target sites

## Setup
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
playwright install chromium
```

## Run everything with one command
```bash
pytest
```

Run only UI or API:
```bash
pytest tests/ui -v
pytest tests/api -v
```

Run UI headed:
```bash
$env:HEADLESS="false"; pytest tests/ui -v   # PowerShell
HEADLESS=false pytest tests/ui -v           # macOS/Linux
```

Screenshots are saved under `evidence/` when the related test captures them. Playwright HTML-independent report output is available in the terminal; use `pytest -v`.

## Test accounts
Password for the SauceDemo seeded users: `secret_sauce`
- `standard_user`
- `locked_out_user`
- `problem_user`
- `performance_glitch_user`

The suite uses `standard_user` for normal purchase flows and `locked_out_user` for the negative login flow. Problem/performance personas are used in targeted diagnostic tests.

## Project layout
```text
saucedemo_qa_submission/
├── README.md
├── requirements.txt
├── pytest.ini
├── manual-test-plan.md
├── test-cases.csv
├── .gitignore
├── tests/
│   ├── conftest.py
│   ├── ui/test_saucedemo.py
│   └── api/test_reqres.py
├── bug-reports/
│   ├── BUG-001-problem-user-product-images.md
│   ├── BUG-002-problem-user-cart-action.md
│   └── BUG-003-performance-user-login-delay.md
└── evidence/
```

## Important evidence and reporting note
The three bug reports are **reproduction-ready reports for known seeded-user problem areas**, not claims that this package author personally reproduced them in this environment. Re-run the stated steps, capture the actual browser screenshot, record browser/OS/date and replace the evidence placeholder before filing them as confirmed GitHub Issues. Do not submit an unverified defect as an observed fact.

## GitHub submission
1. Create a public repository, e.g. `saucedemo-qa-assessment`.
2. Upload this project and commit the files.
3. Create one GitHub Issue per report in `bug-reports/`.
4. Create a GitHub Project (Board) with columns/statuses `To Do`, `In Progress`, `Done`, then add the three issues.
5. Attach the matching screenshot to each issue after reproducing the behavior.
6. Optional: add `.github/workflows/tests.yml` and enable Actions.

## API note
ReqRes is a demo API. Its classic endpoints may be rate-limited or may change access requirements. If the service requires an API key in your environment, set `REQRES_API_KEY` and the test helper will send it as `x-api-key`.
