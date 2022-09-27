from playwright.sync_api import sync_playwright
from pom.PrincipalPage import *
from pom.Elements import *
import os

user1 = {
    "username": "rogerdiazolb",
    "password": "rdiaz"
}

user = {
    "fullName": "Roger Diaz",
    "email": "roger.diaz@cognits.co",
    "currentAddress": "12345",
    "permanentAddress": "abcde"
}


def main():
    with sync_playwright() as p:
        os.system('pytest --html=report.html --self-contained-html')
        browser = p.firefox.launch(headless=False)
        context = browser.new_context(ignore_https_errors=True)
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        page.set_viewport_size({"width": 1500, "height": 1000})
        demo_qa = PrincipalPage(page)
        demo_qa.navigate()
        demo_qa.select_elements()
        elements = Elements(user["fullName"], user["email"], user["currentAddress"], user["permanentAddress"], page)
        elements.open_textbox()
        page.wait_for_timeout(1000)
        elements.enter_info()
        page.wait_for_timeout(1000)
        elements.submit_info()
        page.wait_for_timeout(2000)
        elements.open_checkbox()
        page.wait_for_timeout(1000)
        elements.open_radiobutton()
        page.wait_for_timeout(1000)
        elements.open_web_tables()
        page.wait_for_timeout(1000)
        elements.open_buttons()
        page.wait_for_timeout(1000)
        elements.open_links()
        page.wait_for_timeout(1000)
        elements.open_broken_links_images()
        page.wait_for_timeout(1000)
        elements.open_upload_and_download()
        page.wait_for_timeout(1000)
        elements.open_dinamic_properties()

        page.wait_for_timeout(5000)
        context.tracing.stop(path="trace.zip")
        browser.close()
        os.system('open -a "Google Chrome" report.html')
        # In terminal, execute the following instructions:
        # playwright show-trace trace.zip

        #self.page.wait_for_selector('text=This Month').click()
        #self.page.wait_for_selector('div[class="xwidget_action_icon"]').click()


if __name__ == '__main__':
    main()

'''
from playwright.sync_api import sync_playwright


class TestLogin:
    def run(playwright):
        firefox = playwright.firefox
        browser = firefox.launch()
        context = browser.new_context(ignoreHTTPSErrors=True)
        page = context.new_page()
        page.goto("https://banking-dev104.apps.zions01.development.nymbus.com")
        browser.close()

    with sync_playwright() as playwright:
        run(playwright)
'''
'''
    @pytest.mark.skip_browser("firefox")
    def test_valid_login(self, page):
        login_page = Login_page(page)

        login_page.navigate()
        # encontrar un metodo para hacer una pausa en lugar de
        # security_acceptance
        login_page.security_acceptance()
        login_page.submit_login_form(user)
'''
'''
from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.newPage(ignoreHTTPSErrors=True)
        page.goto("https://banking-dev104.apps.zions01.development.nymbus.com")
        page.wait_for_timeout(5000)

        browser.close()


if __name__ == '__main__':
    main()
'''
