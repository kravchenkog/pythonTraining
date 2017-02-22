from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contacts import ContactsHelper


class AppManager:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(0.5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactsHelper(self)

    def destroy(self):
        self.driver.quit()

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False
