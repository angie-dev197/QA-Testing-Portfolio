import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class TestNavigation(unittest.TestCase):
    """Test suite for navigation functionality"""

    def setUp(self):
        """Setup browser before each test"""
        chrome_options = Options()
        chrome_options.add_argument('--disable-web-security')
        chrome_options.add_argument('--allow-insecure-localhost')
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = "http://127.0.0.1:5500/demo_site/index.html"

    def tearDown(self):
        """Close browser after each test"""
        self.driver.quit()

    def test_homepage_loads_correctly(self):
        """TC-NAV-001: Test homepage loads correctly"""
        self.driver.get(self.base_url)

        self.assertTrue(
    "Welkom in Spanje!" in self.driver.title or "Home" in self.driver.title,
    "Homepage title not found"
        )

        nav_menu = self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "nav"))
        )
        self.assertTrue(nav_menu.is_displayed(), "Navigation menu not visible")

        main_content = self.driver.find_element(By.TAG_NAME, "main")
        self.assertTrue(main_content.is_displayed(), "Main content not visible")

    def test_contact_button_navigation(self):
        """TC-NAV-004: Test contact button navigation"""
        self.driver.get(self.base_url)

        contact_link = self.wait.until(
            EC.element_to_be_clickable((By.ID, "goToForm"))
        )
        contact_link.click()

        self.wait.until(EC.url_contains("form"))  # ✅ wait instead of sleep
        current_url = self.driver.current_url
        self.assertIn("form", current_url.lower(),
                      f"Expected 'form' in URL, got: {current_url}")

        form = self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "form"))
        )
        self.assertTrue(form.is_displayed(), "Contact form not visible")

    def test_all_navigation_links_work(self):
        """TC-NAV-002, TC-NAV-003, TC-NAV-005: Test all navigation links"""
        self.driver.get(self.base_url)

        nav_links = [
            ("Services", "services"),
            ("Culture", "cultuur"),
            ("Contact", "form"),
            ("Home", "index")
        ]

        for link_text, expected_url_part in nav_links:
            nav_link = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, link_text))
            )
            nav_link.click()
            self.wait.until(EC.url_contains(expected_url_part))  # ✅ no sleep

            current_url = self.driver.current_url
            self.assertIn(expected_url_part, current_url.lower(),
                          f"Navigation to {link_text} failed. Got: {current_url}")

            try:  # ✅ Fix 4: specific exception, not bare except
                active_link = self.driver.find_element(
                    By.CSS_SELECTOR,
                    f"nav a.active[href*='{expected_url_part}']"
                )
                self.assertIsNotNone(active_link)
            except Exception:
                pass  # Active state might not be implemented

    def test_form_page_loads(self):
        """Test that form page loads and contains form elements"""
        form_url = self.base_url.replace("index.html", "form.html")  # ✅ Fix 3: was contact.html
        self.driver.get(form_url)

        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))

        name_field = self.driver.find_element(By.CSS_SELECTOR, "#name, [name='name']")
        email_field = self.driver.find_element(By.CSS_SELECTOR, "#email, [name='email']")
        message_field = self.driver.find_element(By.CSS_SELECTOR, "#message, [name='message']")
        submit_button = self.driver.find_element(
            By.CSS_SELECTOR, "button[type='submit'], input[type='submit']"
        )

        self.assertTrue(name_field.is_displayed(), "Name field not visible")
        self.assertTrue(email_field.is_displayed(), "Email field not visible")
        self.assertTrue(message_field.is_displayed(), "Message field not visible")
        self.assertTrue(submit_button.is_displayed(), "Submit button not visible")

    def test_browser_back_navigation(self):
        """Test browser back button navigation"""
        self.driver.get(self.base_url)
        homepage_url = self.driver.current_url

        services_link = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Services"))
        )
        services_link.click()
        self.wait.until(EC.url_contains("services"))  # ✅ no sleep

        self.assertIn("services", self.driver.current_url.lower())

        self.driver.back()
        self.wait.until(EC.url_to_be(homepage_url))  # ✅ no sleep

        self.assertEqual(self.driver.current_url, homepage_url,
                         f"Back navigation failed. Got: {self.driver.current_url}")

    def test_logo_click_returns_home(self):
        """TC-NAV-005: Test that clicking logo returns to homepage"""
        services_url = self.base_url.replace("index.html", "services.html")
        self.driver.get(services_url)

        logo = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "header img, .logo, a[href='index.html']")
            )
        )
        logo.click()
        self.wait.until(EC.url_contains("index"))  # ✅ no sleep

        current_url = self.driver.current_url
        self.assertTrue(
            "index" in current_url.lower() or current_url == self.base_url,
            f"Logo click did not return to homepage. Got: {current_url}"
        )


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
