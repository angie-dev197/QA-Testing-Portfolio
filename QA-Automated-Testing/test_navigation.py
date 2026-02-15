import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class TestNavigation:
    """Test suite for navigation functionality"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup browser before each test"""
        chrome_options = Options()
        chrome_options.add_argument('--disable-web-security')
        chrome_options.add_argument('--allow-insecure-localhost')
        self.driver = webdriver.Chrome(options=chrome_options)
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

        # Base URL - Update this with your actual website path
        self.base_url = "http://localhost:8000/index.html"

        yield

        # Teardown after each test
        self.driver.quit()

    def test_homepage_loads_correctly(self):
        """TC-NAV-001: Test homepage loads correctly"""
        # Navigate to homepage
        self.driver.get(self.base_url)

        # Wait for page to load
        time.sleep(1)

        # Verify page title contains expected text
        assert "Welkom in Spanje!" in self.driver.title or "Home" in self.driver.title,             "Homepage title not found"
        print(f"Page title: {self.driver.title}")
        print(f"Page source preview: {self.driver.page_source[:500]}")

        # Verify key elements are present
        try:
            # Check if navigation menu exists
            nav_menu = self.wait.until(
                EC.presence_of_element_located((By.TAG_NAME, "nav"))
            )
            assert nav_menu.is_displayed(), "Navigation menu not visible"

            # Check if main content exists
            main_content = self.driver.find_element(By.TAG_NAME, "main")
            assert main_content.is_displayed(), "Main content not visible"

            print("✓ Homepage loaded successfully")

        except TimeoutException:
            pytest.fail("Homepage did not load within timeout period")

    def test_contact_button_navigation(self):
        """TC-NAV-004: Test contact button navigation"""
        # Start from homepage
        self.driver.get(self.base_url)

        # Find and click Contact link
        try:
            contact_link = self.wait.until(
                EC.element_to_be_clickable((By.ID, "goToForm"))
            )
            contact_link.click()

            # Wait for navigation
            time.sleep(1)

            # Verify URL contains 'contact'
            current_url = self.driver.current_url
            assert "contact" in current_url.lower(),                 f"Expected 'contact' in URL, got: {current_url}"

            # Verify contact form is present
            form = self.wait.until(
                EC.presence_of_element_located((By.TAG_NAME, "form"))
            )
            assert form.is_displayed(), "Contact form not visible"

            print("✓ Contact navigation successful")

        except TimeoutException:
            pytest.fail("Contact link not found or not clickable")

    def test_all_navigation_links_work(self):
        """TC-NAV-002, TC-NAV-003, TC-NAV-005: Test all navigation links"""
        # Start from homepage
        self.driver.get(self.base_url)

        # Define navigation links to test
        nav_links = [
            ("Services", "services"),
            ("Culture", "culture"),
            ("Contact", "contact"),
            ("Home", "index")
        ]

        for link_text, expected_url_part in nav_links:
            try:
                # Find and click navigation link
                nav_link = self.wait.until(
                    EC.element_to_be_clickable((By.LINK_TEXT, link_text))
                )
                nav_link.click()

                # Wait for navigation
                time.sleep(1)

                # Verify URL
                current_url = self.driver.current_url
                assert expected_url_part in current_url.lower(),                     f"Navigation to {link_text} failed. Expected '{expected_url_part}' in URL, got: {current_url}"

                # Verify active state (if implemented)
                try:
                    active_link = self.driver.find_element(
                        By.CSS_SELECTOR,
                        f"nav a.active[href*='{expected_url_part}'], nav a[href*='{expected_url_part}'].active"
                    )
                    assert active_link is not None
                except:
                    pass  # Active state might not be implemented

                print(f"✓ Navigation to {link_text} successful")

            except TimeoutException:
                pytest.fail(f"Navigation link '{link_text}' not found or not clickable")

    def test_form_page_loads(self):
        """Test that form page loads and contains form elements"""
        # Navigate to contact page
        contact_url = self.base_url.replace("index.html", "contact.html")
        self.driver.get(contact_url)

        # Wait for form to load
        try:
            form = self.wait.until(
                EC.presence_of_element_located((By.TAG_NAME, "form"))
            )

            # Verify form fields exist
            name_field = self.driver.find_element(By.CSS_SELECTOR, "#name, [name='name']")
            email_field = self.driver.find_element(By.CSS_SELECTOR, "#email, [name='email']")
            message_field = self.driver.find_element(By.CSS_SELECTOR, "#message, [name='message']")
            submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit'], input[type='submit']")

            # Verify all fields are displayed
            assert name_field.is_displayed(), "Name field not visible"
            assert email_field.is_displayed(), "Email field not visible"
            assert message_field.is_displayed(), "Message field not visible"
            assert submit_button.is_displayed(), "Submit button not visible"

            print("✓ Form page loaded with all required fields")

        except TimeoutException:
            pytest.fail("Form did not load within timeout period")

    def test_browser_back_navigation(self):
        """Test browser back button navigation"""
        # Start from homepage
        self.driver.get(self.base_url)
        homepage_url = self.driver.current_url

        # Navigate to Services page
        services_link = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Services"))
        )
        services_link.click()
        time.sleep(1)

        # Verify we're on Services page
        assert "services" in self.driver.current_url.lower()

        # Click browser back button
        self.driver.back()
        time.sleep(1)

        # Verify we're back on homepage
        assert self.driver.current_url == homepage_url,             f"Back navigation failed. Expected: {homepage_url}, Got: {self.driver.current_url}"

        print("✓ Browser back navigation successful")

    def test_logo_click_returns_home(self):
        """TC-NAV-005: Test that clicking logo returns to homepage"""
        # Navigate to a non-home page
        services_url = self.base_url.replace("index.html", "services.html")
        self.driver.get(services_url)

        try:
            # Find and click logo (adjust selector based on your HTML structure)
            logo = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "header img, .logo, a[href='index.html']"))
            )
            logo.click()

            # Wait for navigation
            time.sleep(1)

            # Verify we're on homepage
            current_url = self.driver.current_url
            assert "index" in current_url.lower() or current_url == self.base_url,                 f"Logo click did not return to homepage. Current URL: {current_url}"

            print("✓ Logo navigation to homepage successful")

        except TimeoutException:
            pytest.fail("Logo element not found or not clickable")


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v", "--tb=short"])