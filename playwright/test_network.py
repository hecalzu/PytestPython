from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils
from playwright.sync_api import Page

fakePayloadOrderResponse = {"data":[], "message": "No Orders"}

def intercept_response(route):
    route.fulfill(
        json = fakePayloadOrderResponse
    )

def test_network(page: Page):

    #login
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-costumer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("hf1788@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Redfive5..")
    page.get_by_role("button",name="Login").click()

    page.get_by_role("button",name="ORDERS").click()

    order_text = page.locator(".mt-4").text_content()
    print(order_text)
