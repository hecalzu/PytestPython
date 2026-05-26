import os
import sys

import pytest
from playwright.sync_api import Playwright

# Allow tests under playwright/ to import local workspace modules as top-level packages.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "playwright"))

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chromium",
        help="Browser to run tests on: chromium, firefox, or webkit",
    )
    parser.addoption(
        "--url_path",
        action="store",
        default="https://rahulshettyacademy.com/client",
        help="URL path for the application under test",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=True,
        help="Run browser in headless mode",
    )
    parser.addoption(
        "--headed-mode",
        action="store_false",
        dest="headless",
        help="Run browser with UI (headed mode)",
    )

@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param

@pytest.fixture
def browser_instance(playwright: Playwright, request):
    browser_name = request.config.getoption("browser_name")
    url_path = request.config.getoption("url_path")
    headless = request.config.getoption("headless")
    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=headless)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=headless)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=headless)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    context = browser.new_context()
    page = context.new_page()
    page.goto(url_path)
    yield page
    context.close()
    browser.close()
