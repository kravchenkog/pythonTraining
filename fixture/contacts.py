from model.contact import Contact


class ContactsHelper:

    def __init__(self, app):
        self.app = app

    def create_contact(self, contact):
        self.init_contact_creation()
        self.fill_contact_form(contact)
        self.submit_contact_creation()
        self.return_to_home_page()

    def modify(self, counter_of_contact, contact_data):
        self.init_contact_modification(counter_of_contact)
        self.change_value_in_contact_fields(contact_data)
        self.update_button_press()
        self.return_to_home_page()

    def update_button_press(self):
        driver = self.app.driver

        all_buttons = driver.find_elements_by_css_selector("input[value='Update']")
        all_buttons[1].click()

    def init_contact_modification(self, counter_of_contact):
        driver = self.app.driver

        values = driver.find_elements_by_css_selector("td.center img[alt='Edit']")
        values[counter_of_contact].click()

    def change_value_in_contact_fields(self, contact_data):

        self.change_field_value(contact_data.firstname, "firstname")
        self.change_field_value(contact_data.lastname, "lastname")
        self.change_field_value(contact_data.nickname, "nickname")
        self.change_field_value(contact_data.email, "email")
        self.change_field_value(contact_data.home, "home")

    def change_field_value(self, text, value):
        driver = self.app.driver

        if text is not None:
            driver.find_element_by_name(value).clear()
            driver.find_element_by_name(value).send_keys(text)

    def init_contact_creation(self):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()

    def return_to_home_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("home page").click()

    def submit_contact_creation(self):
        driver = self.app.driver

        driver.find_element_by_name("submit").click()