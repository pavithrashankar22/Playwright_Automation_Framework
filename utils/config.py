import os

class Config:
    BASE_URL = os.environ.get("BASE_URL", "https://automationexercise.com")
    API_BASE_URL = os.environ.get("API_BASE_URL", "https://automationexercise.com/api")