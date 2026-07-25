from api.account_api import AccountAPI
import pytest
import uuid
from utils.config import Config
from utils.test_data import load_account_data

def test_login_api_user(signup_login_page, page):
    user_name = f"User {uuid.uuid4()}"
    user_email = f"user{uuid.uuid4()}@example.com"

    create_account_data = load_account_data()[0]
    create_account_data["name"] = user_name
    create_account_data["email"] = user_email

    response = AccountAPI.create_account(create_account_data)
    assert response.json()["responseCode"] == 201, f"Account creation failed: {response.json()}"

    signup_login_page.go_to(f"{Config.BASE_URL}/login")
    signup_login_page.login(user_email, create_account_data["password"])
    signup_login_page.expect_logged_in_as_visible(user_name)