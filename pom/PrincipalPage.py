url = 'https://demoqa.com/'
elementsButton = 'text=Elements'
formsButton = 'text=Forms'
afwButton = 'Alerts, Frame & Windows'
widgetsButton = 'Widgets'
interactionsButton = 'Interactions'
bsaButton = 'Book Store Application'


class PrincipalPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(url)

    def select_elements(self):
        self.page.wait_for_selector(elementsButton).click()

    def select_forms(self):
        self.page.wait_for_selector(formsButton).click()

    def select_afw(self):
        self.page.wait_for_selector(afwButton).click()

    def select_widgets(self):
        self.page.wait_for_selector(widgetsButton).click()

    def select_interactions(self):
        self.page.wait_for_selector(interactionsButton).click()

    def select_bsa(self):
        self.page.wait_for_selector(bsaButton).click()
