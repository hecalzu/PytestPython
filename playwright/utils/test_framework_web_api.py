import json
import os
import sys

from playwright.sync_api import Playwright, expect
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from apiBase import APIUtils
from pageObjects.login import LoginPage
from pageObjects.dashboard import DashboardPage

#create order -> orderId

with open("playwright/data/credentials.json") as f:
        data = json.load(f)
        print(data)
        user_credentials_list  = data["user_credentials"]

@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(playwright:Playwright, user_credentials, browser_instance):

    apiUtils = APIUtils()
    
    orderId = apiUtils.createOrder(playwright, user_credentials)
    
    loginPage = LoginPage(browser_instance)
    loginPage.navigate()
    
    dashboardPage = loginPage.login(user_credentials)
    orderHistoryPage = dashboardPage.goToOrders()

    #orders history
    orderDetailsPage = orderHistoryPage.selectOrder(orderId)
    orderDetailsPage.verifyOrderMessage()
