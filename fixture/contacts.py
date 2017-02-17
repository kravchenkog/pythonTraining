class ContactsHelper:

    def __init__(self, app):
        self.app = app

    def create_contact(self, contact):
        driver = self.app.driver

        self.init_contact_creation()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(contact.lastname)
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(contact.nickname)
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(contact.email)
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys(contact.home)
        self.submit_contact_creation()
        self.return_to_home_page()

    def init_contact_creation(self):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()

    def return_to_home_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("home page").click()

    def submit_contact_creation(self):
        driver = self.app.driver

        driver.find_element_by_name("submit").click()