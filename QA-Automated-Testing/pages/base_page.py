from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Base class inherited by all page objects."""

    def __init__(self, driver, base_url="http://127.0.0.1:5500/demo_site"):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)

    def navigate_to(self, path="index.html"):
        self.driver.get(f"{self.base_url}/{path}")

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def wait_for_url_contains(self, text):
        self.wait.until(EC.url_contains(text))

    def wait_for_url_to_be(self, url):
        self.wait.until(EC.url_to_be(url))

    def get_current_url(self):
        return self.driver.current_url

    def go_back(self):
        self.driver.back()
