# Automation Exercise Framework

This project is a Python-based test automation framework for validating the Automation Exercise application through both API and UI tests. It uses pytest as the core test runner, requests for API interactions, and Playwright for browser-based UI testing. Allure integration is also configured for rich reporting.

## Project Overview

The framework is organized to support:

- API testing for account creation and login flows
- UI testing for signup and login scenarios
- Reusable page objects and test data helpers
- Reporting through Allure

## Project Structure

```text
.
├── api/
│   └── account_api.py
├── pages/
│   ├── base_page.py
│   ├── signup_login_page.py
│   ├── signup_page.py
│   └── __init__.py
├── tests/
│   ├── api/
│   │   └── test_account_api.py
│   ├── ui/
│   │   ├── test_login.py
│   │   └── test_signup.py
├── test_data/
│   └── account_data.json
├── utils/
│   ├── config.py
│   ├── test_data.py
│   └── __init__.py
├── conftest.py
├── pytest.ini
├── requirements.txt
```

## Prerequisites

Make sure you have the following installed:

- Python 3.9+
- pip
- A compatible browser for Playwright (installed automatically via Playwright setup)

## Installation

1. Clone the repository.
2. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Install Playwright browsers:

```bash
playwright install
```

## Configuration

The framework uses configuration values from the utilities package, including the base URL and API endpoint settings. You can adjust these values in:

- [utils/config.py](utils/config.py)

## Running Tests

Run all tests:

```bash
pytest
```

Run only API tests:

```bash
pytest -m api
```

Run only UI tests:

```bash
pytest -m ui
```

Run a specific test file:

```bash
pytest tests/api/test_account_api.py
```

## Allure Reporting

This project is configured to generate Allure results during pytest runs.

To run tests with Allure output:

```bash
pytest
```

To generate the interactive HTML dashboard from the raw results, run:

```powershell
./generate_allure_report.ps1
```

This script uses the locally installed Allure CLI and writes the report to the allure-report folder.

To open the report locally:

```powershell
Start-Process allure-report\index.html
```

## Test Design Notes

- API tests are implemented in [tests/api/test_account_api.py](tests/api/test_account_api.py)
- UI tests are implemented in [tests/ui/test_login.py](tests/ui/test_login.py) and [tests/ui/test_signup.py](tests/ui/test_signup.py)
- Shared test data is loaded from [test_data/account_data.json](test_data/account_data.json)
- Page objects are defined under [pages](pages)

## Notes

- The project uses pytest markers such as `smoke`, `regression`, `api`, and `ui`.
- The pytest configuration is stored in [pytest.ini](pytest.ini).

## CI/CD with GitHub Actions

A GitHub Actions workflow is included at [.github/workflows/pytest-allure.yml](.github/workflows/pytest-allure.yml). It will:

- install dependencies
- run the pytest suite
- generate an Allure report
- publish the report to GitHub Pages
- upload the report as a workflow artifact
