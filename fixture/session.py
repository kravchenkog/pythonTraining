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
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_home_page(self):
        driver = self.app.driver
        driver.get('http://localhost:8080/addressbook/')

    def logout(self):
        driver = self.app.driver
        driver.find_element_by_link_text("Logout").click()