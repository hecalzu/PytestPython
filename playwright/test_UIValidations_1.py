from time import sleep

from playwright.sync_api import Page, expect

def test_UIValidationDynamicScript(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()    
    page.get_by_role("button", name="Sign in").click()

    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneProduct.get_by_role("button").click()

    iphoneProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    iphoneProduct.get_by_role("button").click()

    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)
    sleep(5)

def test_childWindowHandler(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as newPage_info:
        # Click on the "Free Access" blinking text link
        page.get_by_text("Free Access").click()
        childPage = newPage_info.value
        text = childPage.locator(".red").text_content()
        words = text.split("at")
        print(words)
        email = words[1].strip().split(" ")[0]
        assert email == "mentor@rahulshettyacademy.com"
