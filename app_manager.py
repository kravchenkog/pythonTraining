from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from group import Group
from contact import Contact


class AppManager:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(60)
        self.base_url = "http://localhost:8080"

    def create_group(self, group):
        self.open_group_page()
        self.init_group_creation()
        self.fill_group_form(group)
        self.submit_group_creation()
        self.return_to_group_page()

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Logout").click()

    def return_to_group_page(self):
        driver = self.driver
        driver.find_element_by_link_text("group page").click()

    def submit_group_creation(self):
        driver = self.driver
        driver.find_element_by_name("submit").click()

    def fill_group_form(self, group):
        driver = self.driver
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)

    def init_group_creation(self):
        driver = self.driver
        driver.find_element_by_name("new").click()

    def open_group_page(self):
        driver = self.driver
        driver.find_element_by_link_text("groups").click()

    def login(self, user_name, password):
        driver = self.driver

        self.open_home_page()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(user_name)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_home_page(self):
        driver = self.driver

        driver.get(self.base_url + "/addressbook/")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True
    # For contacts

    def create_contact(self, contact):
        driver = self.driver

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
        driver = self.driver
        driver.find_element_by_link_text("add new").click()

    def return_to_home_page(self):
        driver = self.driver
        driver.find_element_by_link_text("home page").click()

    def submit_contact_creation(self):
        driver = self.driver

        driver.find_element_by_name("submit").click()

    def destroy(self):
        self.driver.quit()