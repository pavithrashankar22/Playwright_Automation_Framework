import pytest
from pages.signup_login_page import SignupLoginPage
from pages.signup_page import SignupPage


@pytest.fixture
def signup_login_page(page):
    return SignupLoginPage(page)

@pytest.fixture
def signup_page(page):
    return SignupPage(page)