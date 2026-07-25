from pages.base_page import BasePage
from playwright.sync_api import expect

class SignupLoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.login_form = page.locator("form").filter(has_text="Login")
        self.signup_form = page.locator("form").filter(has_text="Signup")

        self.login_email_input = self.login_form.get_by_placeholder("Email Address")
        self.login_password_input = self.login_form.get_by_role("textbox", name="Password")
        self.login_button = self.login_form.get_by_role("button", name="Login")

        self.signup_name_input = self.signup_form.get_by_role("textbox", name="Name")
        self.signup_email_input = self.signup_form.get_by_placeholder("Email Address")
        self.signup_button = self.signup_form.get_by_role("button", name="Signup")

    def login(self, email, password):
        self.login_email_input.fill(email)
        self.login_password_input.fill(password)
        self.login_button.click()

    def start_signup(self, name, email):
        self.signup_name_input.fill(name)
        self.signup_email_input.fill(email)
        self.signup_button.click()
      
    def expect_account_info_form_visible(self):
        expect(self.page.get_by_role("heading", name="Enter Account Information")).to_be_visible()
