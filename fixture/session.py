class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, user_name, password):
        driver = self.app.driver

        self.open_home_page()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(user_name)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_css_selector("input[value='Login']").click()

    def open_home_page(self):
        driver = self.app.driver
        driver.get('http://localhost:8080/addressbook/')

    def logout(self):
        driver = self.app.driver
        driver.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        driver = self.app.driver

        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        driver = self.app.driver

        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()

        self.login(username, password)

    def is_logged_in_as(self, username):

        if username == self.get_logged_username():
            return True
        else:
            return False

    def is_logged_in(self):
        driver = self.app.driver
        return len(driver.find_elements_by_link_text("Logout")) > 0

    def get_logged_username(self):
        driver = self.app.driver
        text_username = driver.find_element_by_css_selector("form[class='header'] b").text[1:-1]

        return text_username