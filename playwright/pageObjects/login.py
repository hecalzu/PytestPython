from .dashboard import DashboardPage


class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self, user_credentials):
        self.page.get_by_placeholder("email@example.com").fill(user_credentials["userEmail"])
        self.page.get_by_placeholder("enter your passsword").fill(user_credentials["userPassword"])
        self.page.get_by_role("button",name="Login").click()
        dashboard = DashboardPage(self.page)
        return dashboard
    
    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")