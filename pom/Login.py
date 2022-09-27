#from playwright.sync_api import sync_playwright
import var

class Login:
    def __init__(self, username, password, page):
        self.username = username
        self.password = password
        self.page = page



    def login(self):
        self.page.locator('input[name="login"]').fill(self.username)
        self.page.locator('input[name="password"]').fill(self.password)
        self.page.locator('text=Enter')
        self.page.locator("button:has-text(\"Elements\")").click()
