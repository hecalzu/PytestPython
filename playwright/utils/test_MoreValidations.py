from playwright.sync_api import Page, expect
def test_UIchecks(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button",name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #Alerts
    page.on("dialog",lambda dialog:dialog.accept())
    page.get_by_role("button",name="Confirm").click()

    #Mouse hover
    page.locator("#mousehover").hover()
    page.get_by_role("link",name="Top").click()

    #Frame handling
    pageframe = page.frame_locator("#courses-iframe")
    pageframe.get_by_role("link",name="All Access plan").click()
    expect(pageframe.locator("body")).to_contain_text("Happy")

    #Check price value
    #identify price column
    #identify rice column
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
            priceColumnIndex = index
            print(f"Price column value is: {index}")
            break
    ricerow = page.locator("tr").filter(has_text="Rice")
    expect(ricerow.locator("td").nth(priceColumnIndex)).to_have_text("37")