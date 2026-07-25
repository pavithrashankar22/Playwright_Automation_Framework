import requests
from utils.config import Config

class AccountAPI:
    CREATE_ACCOUNT_URL = f"{Config.API_BASE_URL}/createAccount"

    @staticmethod
    def create_account(account_data: dict):
        payload = {
            "name": account_data["name"],
            "email": account_data["email"],
            "password": account_data["password"],
            "title": "Mr" if account_data.get("gender", "male").lower() == "male" else "Mrs",
            "birth_date": account_data.get("day", "1"),
            "birth_month": account_data.get("month", "1"),
            "birth_year": account_data.get("year", "1990"),
            "firstname": account_data.get("first_name", ""),
            "lastname": account_data.get("last_name", ""),
            "company": account_data.get("company", ""),
            "address1": account_data.get("address1", ""),
            "address2": account_data.get("address2", ""),
            "country": account_data.get("country", ""),
            "zipcode": account_data.get("zipcode", ""),
            "state": account_data.get("state", ""),
            "city": account_data.get("city", ""),
            "mobile_number": account_data.get("mobile_number", ""),
        }
        response = requests.post(AccountAPI.CREATE_ACCOUNT_URL, data=payload)
        return response