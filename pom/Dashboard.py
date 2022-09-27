class Dashboard:
    def __init__(self, page):
        self.page = page

    def clickondashboard(self):
        self.page.wait_for_selector('#topMenu-item-bizhub').click()
        self.page.wait_for_selector('#ui-id-47').click()

    def hoveronmoneyin(self):
        self.page.wait_for_selector('div[class="icon-header-support"]').hover()
        self.page.wait_for_timeout(1000)

    def moneyingraphfilter(self):
        self.page.wait_for_selector('div[class="xwidget_action_icon"]').click()
        self.page.wait_for_timeout(1000)
        self.page.wait_for_selector('text=Past 2 Weeks').click()
        self.page.wait_for_selector('div[class="xwidget_action_icon"]').click()
        self.page.wait_for_timeout(1000)
        self.page.wait_for_selector('text=This Month').click()
        self.page.wait_for_selector('div[class="xwidget_action_icon"]').click()
        self.page.wait_for_timeout(1000)
        self.page.wait_for_selector('text=Rolling 30 Days').click()
        self.page.wait_for_selector('div[class="xwidget_action_icon"]').click()
        self.page.wait_for_timeout(1000)
        self.page.wait_for_selector('text=Past 6 Months').click()

    def managecustomrange(self):
        self.page.wait_for_selector('div[class="xwidget_action_icon"]').click()
        self.page.wait_for_timeout(1000)
        self.page.wait_for_selector('text=Manage Custom Range').click()
        self.page.wait_for_timeout(1000)
      #  self.page.wait_for_selector().click()




    #usar variables para guardar los identificadores y usarlos en los diferentes metodos
