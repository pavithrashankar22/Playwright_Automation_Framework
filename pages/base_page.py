from playwright.sync_api import expect

class BasePage:
    def __init__(self,page):
        self.page = page
    
    def go_to(self,url):
        self.page.goto(url)
    def get_title(self):
        return self.page.title()
    def get_url(self):
        return self.page.url
    def get_element(self, selector):
        return self.page.locator(selector)

    def expect_logged_in_as_visible(self, name):
        expect(self.page.get_by_text(f"Logged in as {name}")).to_be_visible()