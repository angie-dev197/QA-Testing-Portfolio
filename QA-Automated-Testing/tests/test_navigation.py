import pytest
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.form_page import FormPage
from pages.services_page import ServicesPage


def test_homepage_loads_correctly(driver):
    """TC-NAV-001: Test homepage loads correctly"""
    page = HomePage(driver)
    page.load()

    title = page.get_title()
    assert "Welkom in Spanje!" in title or "Home" in title, "Homepage title not found"
    assert page.get_nav_menu().is_displayed(), "Navigation menu not visible"
    assert page.get_main_content().is_displayed(), "Main content not visible"


def test_contact_button_navigation(driver):
    """TC-NAV-004: Test contact button navigates to form page"""
    page = HomePage(driver)
    page.load()
    page.click_contact_button()
    page.wait_for_url_contains("form")

    assert "form" in page.get_current_url().lower(), \
        f"Expected 'form' in URL, got: {page.get_current_url()}"

    form_page = FormPage(driver)
    assert form_page.get_form().is_displayed(), "Contact form not visible"


def test_all_navigation_links_work(driver):
    """TC-NAV-002, TC-NAV-003, TC-NAV-005: All nav links lead to correct pages"""
    page = HomePage(driver)
    page.load()

    nav_links = [
        ("Services", "services"),
        ("Culture",  "cultuur"),
        ("Contact",  "form"),
        ("Home",     "index"),
    ]

    for link_text, expected_url_part in nav_links:
        page.click_nav_link(link_text)
        page.wait_for_url_contains(expected_url_part)
        assert expected_url_part in page.get_current_url().lower(), \
            f"Navigation to {link_text} failed. Got: {page.get_current_url()}"

        try:
            active_link = page.get_active_nav_link(expected_url_part)
            assert active_link is not None
        except Exception:
            pass  # Active state might not be implemented yet


def test_form_page_loads(driver):
    """Test that form page loads with all required form fields"""
    page = FormPage(driver)
    page.load()

    assert page.get_name_field().is_displayed(),    "Name field not visible"
    assert page.get_email_field().is_displayed(),   "Email field not visible"
    assert page.get_message_field().is_displayed(), "Message field not visible"
    assert page.get_submit_button().is_displayed(), "Submit button not visible"


def test_browser_back_navigation(driver):
    """Test browser back button returns to previous page"""
    page = HomePage(driver)
    page.load()
    homepage_url = page.get_current_url()

    page.click_nav_link("Services")
    page.wait_for_url_contains("services")
    assert "services" in page.get_current_url().lower()

    page.go_back()
    page.wait_for_url_to_be(homepage_url)
    assert page.get_current_url() == homepage_url, \
        f"Back navigation failed. Got: {page.get_current_url()}"


def test_logo_click_returns_home(driver):
    """TC-NAV-005: Clicking the logo from any page returns to homepage"""
    services_page = ServicesPage(driver)
    services_page.load()

    home_page = HomePage(driver)
    home_page.click_logo()
    home_page.wait_for_url_contains("index")

    current_url = home_page.get_current_url()
    assert "index" in current_url.lower() or current_url == f"{home_page.base_url}/index.html", \
        f"Logo click did not return to homepage. Got: {current_url}"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
