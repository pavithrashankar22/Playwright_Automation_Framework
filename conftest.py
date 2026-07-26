import os
import subprocess
from pathlib import Path

import pytest
from pages.signup_login_page import SignupLoginPage
from pages.signup_page import SignupPage


@pytest.fixture
def signup_login_page(page):
    return SignupLoginPage(page)


@pytest.fixture
def signup_page(page):
    return SignupPage(page)


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    if os.environ.get("SKIP_ALLURE_REPORT") == "1":
        return

    repo_root = Path(__file__).resolve().parent
    script_path = repo_root / "generate_allure_report.ps1"
    if not script_path.exists():
        return

    try:
        subprocess.run(
            ["powershell", "-ExecutionPolicy", "Bypass", "-File", str(script_path)],
            cwd=str(repo_root),
            check=True,
            capture_output=True,
            text=True,
        )
    except Exception:
        pass