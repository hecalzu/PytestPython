from playwright.sync_api import Playwright, expect
import time

from utils.apiBase import APIUtils
from playwright.sync_api import Page

fakePayloadOrderResponse = {"data":[], "message": "No Orders"}

def intercept_response(route):
    route.fulfill(
        json = fakePayloadOrderResponse
    )

def interceptRequest(route):
    route.continue_(url="https://rahulshettyacademy.com/client/#/dashboard/order-details/6a0cc35917ee3e78ba895794")

def test_network2(page: Page):

    #login
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",interceptRequest)
    page.get_by_placeholder("email@example.com").fill("hf1788@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Redfive5..")
    page.get_by_role("button",name="Login").click()

    page.get_by_role("button",name="ORDERS").click()
    page.get_by_role("button",name="View").first.click()

    time.sleep(5)

def test_session_storage(playwright: Playwright):
    api_utils =APIUtils()
    token = api_utils.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #script to inject token into session storage
    page.add_init_script(f"""window.localStorage.setItem('token', '{token}');""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button",name="ORDERS").click()
    page.get_by_text("Your Orders").to_be_visible()
    browser.close()


