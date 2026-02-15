"""
Pytest configuration file for Selenium tests
Handles screenshots on test failure and reporting
"""

import pytest
from datetime import datetime
import os


# Create screenshots directory if it doesn't exist
SCREENSHOTS_DIR = "test-results/screenshots"
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture screenshot on test failure
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Get the test instance
        if hasattr(item, 'funcargs'):
            if 'self' in item.funcargs:
                test_instance = item.funcargs['self']
                if hasattr(test_instance, 'driver'):
                    # Generate screenshot filename
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    test_name = item.name
                    screenshot_name = f"{test_name}_{timestamp}_FAILED.png"
                    screenshot_path = os.path.join(SCREENSHOTS_DIR, screenshot_name)

                    # Take screenshot
                    try:
                        test_instance.driver.save_screenshot(screenshot_path)
                        print(f"\n Screenshot saved: {screenshot_path}")
                    except Exception as e:
                        print(f"\n Could not save screenshot: {e}")


def pytest_configure(config):
    """
    Add custom markers and configure reporting
    """
    config.addinivalue_line("markers", "navigation: Navigation test cases")
    config.addinivalue_line("markers", "form: Form validation test cases")
    config.addinivalue_line("markers", "responsive: Responsive design test cases")