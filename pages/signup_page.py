from pages.base_page import BasePage
from playwright.sync_api import expect

class SignupPage(BasePage):

    def __init__(self,page):
        super().__init__(page)
        self.id_gender_male = page.get_by_label("Mr.")
        self.id_gender_female = page.get_by_label("Mrs.")
        self.name=page.locator("#name")
        self.email=page.locator("#email")
        self.password=page.locator("#password")
        self.days=page.locator("#days")
        self.months=page.locator("#months") 
        self.years=page.locator("#years")
        self.newsletter=page.locator("#newsletter")
        self.optin=page.locator("#optin")   
        self.first_name=page.locator("#first_name")
        self.last_name=page.locator("#last_name")
        self.company=page.locator("#company")
        self.address1=page.locator("#address1")
        self.address2=page.locator("#address2")
        self.country=page.locator("#country")
        self.state=page.locator("#state")
        self.city=page.locator("#city") 
        self.zipcode=page.locator("#zipcode")
        self.mobile_number=page.locator("#mobile_number")
        self.create_account_button=page.locator("button").filter(has_text="Create Account")

    def fill_signup_form(self, account_data: dict):
        gender = account_data.get("gender", "male").lower()
        if gender == "male":
            self.id_gender_male.check()
        else:
            self.id_gender_female.check()
        self.name.fill(account_data.get("name", ""))
        #self.email.fill(account_data.get("email", ""))
        self.password.fill(account_data.get("password", ""))
        self.days.select_option(account_data.get("day", ""))
        self.months.select_option(account_data.get("month", ""))
        self.years.select_option(account_data.get("year", ""))
        if account_data.get("newsletter", False):
            self.newsletter.check()
        if account_data.get("optin", False):
            self.optin.check()
        self.first_name.fill(account_data.get("first_name", ""))
        self.last_name.fill(account_data.get("last_name", ""))
        self.company.fill(account_data.get("company", ""))
        self.address1.fill(account_data.get("address1", ""))
        self.address2.fill(account_data.get("address2", ""))
        self.country.select_option(account_data.get("country", ""))
        self.state.fill(account_data.get("state", ""))
        self.city.fill(account_data.get("city", ""))
        self.zipcode.fill(account_data.get("zipcode", ""))
        self.mobile_number.fill(account_data.get("mobile_number", ""))
        self.create_account_button.click()

    
    def expect_account_created_visible(self):
        expect(self.page.get_by_role("heading", name="Account Created!")).to_be_visible()
    
    def click_continue_button(self):
        self.page.get_by_role("link", name="Continue").click()
    
    
    





