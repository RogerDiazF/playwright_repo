textBox = '#item-0'
userNameField = '#userName'
userEmailField = '#userEmail'
currentAddressField = '#currentAddress'
permanentAddressField = '#permanentAddress'
submitButton = "button:has-text(\"Submit\")"

checkBox = '#item-1'
radioButton = '#item-2'
webTables = '#item-3'
buttons = '#item-4'
links = '#item-5'
brokenLinksImages = '#item-6'
uploadAndDownload = '#item-7'
dynamicProperties = '#item-8'


class Elements:
    def __init__(self, full_name, email, current_address, permanent_address, page):
        self.full_name = full_name
        self.email = email
        self.current_address = current_address
        self.permanent_address = permanent_address
        self.page = page

    def open_textbox(self):
        self.page.wait_for_selector(textBox).click()

    def enter_info(self):
        self.page.locator(userNameField).fill(self.full_name)
        self.page.locator(userEmailField).fill(self.email)
        self.page.locator(currentAddressField).fill(self.current_address)
        self.page.locator(permanentAddressField).fill(self.permanent_address)

    def submit_info(self):
        self.page.locator(submitButton).click()


    def open_checkbox(self):
        self.page.wait_for_selector(checkBox).click()

    def open_radiobutton(self):
        self.page.wait_for_selector(radioButton).click()

    def open_web_tables(self):
        self.page.wait_for_selector(webTables).click()

    def open_buttons(self):
        self.page.wait_for_selector(buttons).click()

    def open_links(self):
        self.page.wait_for_selector(links).click()

    def open_broken_links_images(self):
        self.page.wait_for_selector(brokenLinksImages).click()

    def open_upload_and_download(self):
        self.page.wait_for_selector(uploadAndDownload).click()

    def open_dinamic_properties(self):
        self.page.wait_for_selector(dynamicProperties).click()
