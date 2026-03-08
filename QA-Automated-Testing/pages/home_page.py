from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    NAV_MENU       = (By.TAG_NAME, "nav")
    MAIN_CONTENT   = (By.TAG_NAME, "main")
    CONTACT_BUTTON = (By.ID, "goToForm")
    LOGO           = (By.CSS_SELECTOR, "header img, .logo, a[href='index.html']")

    NAV_LINKS = {
        "Services": "services",
        "Culture":  "cultuur",
        "Contact":  "form",
        "Home":     "index",
    }

    def load(self):
        self.navigate_to("index.html")

    def get_title(self):
        return self.driver.title

    def get_nav_menu(self):
        return self.find_element(self.NAV_MENU)

    def get_main_content(self):
        return self.find_element(self.MAIN_CONTENT)

    def click_contact_button(self):
        self.click_element(self.CONTACT_BUTTON)

    def click_nav_link(self, link_text):
        self.click_element((By.LINK_TEXT, link_text))

    def get_active_nav_link(self, url_part):
        return self.driver.find_element(
            By.CSS_SELECTOR, f"nav a.active[href*='{url_part}']"
        )

    def click_logo(self):
        self.click_element(self.LOGO)
