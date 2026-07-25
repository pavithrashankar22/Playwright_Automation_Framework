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
