from pages.base_page import BasePage


class ServicesPage(BasePage):
    def load(self):
        self.navigate_to("services.html")
