from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from group import  Group
import unittest


class Untitled3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8080"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_group_creation(self):
        driver = self.driver

        self.open_home_page(driver)
        self.login(driver, user_name="admin", password="secret")
        self.open_group_page(driver)
        self.create_group(driver, Group(name="test name", header="test header", footer="test footer"))
        self.return_to_group_page(driver)
        self.logout(driver)

    def test_empty_group_creation(self):
        driver = self.driver

        self.open_home_page(driver)
        self.login(driver, user_name="admin", password="secret")
        self.open_group_page(driver)
        self.create_group(driver, Group(name="", header="", footer=""))
        self.return_to_group_page(driver)
        self.logout(driver)

    def create_group(self, driver, group):
        self.init_group_creation(driver)
        self.fill_group_form(driver, group)
        self.submit_group_creation(driver)

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def return_to_group_page(self, driver):
        driver.find_element_by_link_text("group page").click()

    def submit_group_creation(self, driver):
        driver.find_element_by_name("submit").click()

    def fill_group_form(self, driver, group):
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)

    def init_group_creation(self, driver):
        driver.find_element_by_name("new").click()

    def open_group_page(self, driver):
        driver.find_element_by_link_text("groups").click()

    def login(self, driver, user_name, password):
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(user_name)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_home_page(self, driver):
        driver.get(self.base_url + "/addressbook/")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
