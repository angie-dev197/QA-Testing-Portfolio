from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FormPage(BasePage):
    FORM           = (By.TAG_NAME, "form")
    NAME_FIELD     = (By.CSS_SELECTOR, "#name, [name='name']")
    EMAIL_FIELD    = (By.CSS_SELECTOR, "#email, [name='email']")
    MESSAGE_FIELD  = (By.CSS_SELECTOR, "#message, [name='message']")
    SUBMIT_BUTTON  = (By.CSS_SELECTOR, "button[type='submit'], input[type='submit']")

    def load(self):
        self.navigate_to("form.html")

    def get_form(self):
        return self.find_element(self.FORM)

    def get_name_field(self):
        return self.find_element(self.NAME_FIELD)

    def get_email_field(self):
        return self.find_element(self.EMAIL_FIELD)

    def get_message_field(self):
        return self.find_element(self.MESSAGE_FIELD)

    def get_submit_button(self):
        return self.find_element(self.SUBMIT_BUTTON)
