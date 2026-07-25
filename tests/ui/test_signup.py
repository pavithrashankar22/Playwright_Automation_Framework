import uuid
import pytest
from utils.config import Config
from utils.test_data import load_account_data


@pytest.mark.parametrize("account_data", load_account_data(), ids=lambda d: d["case_name"])
def test_signup_new_user(page, signup_login_page, signup_page, account_data):
    signup_login_page.go_to(f"{Config.BASE_URL}/login")

    name = f"User {uuid.uuid4()}"
    email = f"user{uuid.uuid4()}@example.com"

    signup_login_page.start_signup(name, email)
    signup_login_page.expect_account_info_form_visible()
    
    account_data["name"] = name
    account_data["email"] = email
    #page.pause()
    

    signup_page.fill_signup_form(account_data)
    signup_page.expect_account_created_visible()
    #page.pause()
    signup_page.click_continue_button()
    signup_page.expect_logged_in_as_visible(name)