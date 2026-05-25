import pytest
from playwright.sync_api import Playwright

@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param

def preSetupWork():
    # Perform any necessary setup work here
    pass

@pytest.fixture(scope="session")
def browser_instance(playwright: Playwright, request):
    request.config.getoption("browser_name")
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()

