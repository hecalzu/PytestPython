import pytest
from playwright.sync_api import Playwright

@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param

def preSetupWork():
    # Perform any necessary setup work here
    pass

@pytest.fixture
def browser_instance(playwright: Playwright, request):
    browser_name = request.config.getoption("browser_name")
    url_path = request.config.getoption("url_path")
    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=False)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    context = browser.new_context()
    page = context.new_page()
    page.goto(url_path)
    yield page
    context.close()
    browser.close()

