import uuid
import requests
from api.account_api import AccountAPI
from utils.config import Config
from utils.test_data import load_account_data



def test_create_account_with_valid_data():
    base_data = load_account_data()[0]
    unique_suffix = uuid.uuid4().hex[:8]

    account_data = {
        **base_data,
        "name": f"Test User {unique_suffix}",
        "email": f"test_{unique_suffix}@example.com"
    }

    response = AccountAPI.create_account(account_data)

    assert response.json()["responseCode"] == 201


def test_create_account_with_duplicate_email():
    base_data = load_account_data()[0]
    unique_suffix = uuid.uuid4().hex[:8]
    email = f"test_{unique_suffix}@example.com"

    first_account_data = {
        **base_data,
        "name": f"Test User {unique_suffix}",
        "email": email
    }
    second_account_data = {
        **base_data,
        "name": f"Test User {unique_suffix} 2",
        "email": email
    }

    first_response = AccountAPI.create_account(first_account_data)
    second_response = AccountAPI.create_account(second_account_data)

    assert second_response.json()["responseCode"] == 400
    assert "already exists" in second_response.json()["message"].lower()


def test_create_account_missing_password():
    base_data = load_account_data()[0]
    unique_suffix = uuid.uuid4().hex[:8]

    account_data = {
        **base_data,
        "name": f"Test User {unique_suffix}",
        "email": f"test_{unique_suffix}@example.com"
    }
    account_data.pop("password")

    response = AccountAPI.create_account(account_data)
    response_body = response.json()

    print(f"Missing password response body: {response_body}")
    assert response_body["responseCode"] == 201


def test_create_account_invalid_email_format():
    base_data = load_account_data()[0]
    unique_suffix = uuid.uuid4().hex[:8]

    account_data = {
        **base_data,
        "name": f"Test User {unique_suffix}",
        "email": "notanemail"
    }

    response = AccountAPI.create_account(account_data)

    print(f"Invalid email status code: {response.status_code}")
    print(f"Invalid email response body: {response.json()}")


def test_create_account_missing_email():
    base_data = load_account_data()[0]
    unique_suffix = uuid.uuid4().hex[:8]

    account_data = {
        **base_data,
        "name": f"Test User {unique_suffix}",
        "email": f"test_{unique_suffix}@example.com"
    }
    account_data.pop("email")

    response = AccountAPI.create_account(account_data)
    response_body = response.json()

    print(f"Missing email response body: {response_body}")
    assert response_body["responseCode"] != 201


def test_create_account_empty_payload():
    response = AccountAPI.create_account({})
    response_body = response.json()

    print(f"Empty payload response body: {response_body}")
    assert response_body["responseCode"] != 201


def test_login_with_existing_user_incorrect_password():
    base_data = load_account_data()[0]
    unique_suffix = uuid.uuid4().hex[:8]
    email = f"test_{unique_suffix}@example.com"

    account_data = {
        **base_data,
        "name": f"Test User {unique_suffix}",
        "email": email
    }

    create_response = AccountAPI.create_account(account_data)
    assert create_response.json()["responseCode"] == 201

    login_payload = {
        "email": email,
        "password": "wrong_password"
    }

    response = requests.post(
        f"{Config.API_BASE_URL}/verifyLogin",
        data=login_payload
    )
    response_body = response.json()

    print(f"Incorrect password login response body: {response_body}")
    assert response_body["responseCode"] != 201


def test_login_with_existing_user_correct_password():
    base_data = load_account_data()[0]
    unique_suffix = uuid.uuid4().hex[:8]
    email = f"test_{unique_suffix}@example.com"

    account_data = {
        **base_data,
        "name": f"Test User {unique_suffix}",
        "email": email
    }

    create_response = AccountAPI.create_account(account_data)
    assert create_response.json()["responseCode"] == 201

    login_payload = {
        "email": email,
        "password": base_data.get("password", "")
    }

    response = requests.post(
        f"{Config.API_BASE_URL}/verifyLogin",
        data=login_payload
    )
    response_body = response.json()

    print(f"Correct password login response body: {response_body}")
    assert response_body["responseCode"] == 200


def test_login_with_non_existing_email():
    login_payload = {
        "email": "doesnotexist@example.com",
        "password": "any_password"
    }

    response = requests.post(
        f"{Config.API_BASE_URL}/verifyLogin",
        data=login_payload
    )
    response_body = response.json()

    print(f"Non-existing email login response body: {response_body}")
    assert response_body["responseCode"] != 200
