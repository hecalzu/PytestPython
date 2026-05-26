
import pytest

from utils.apiBaseFramework import APIUtils
from pageObjects.login import LoginPage
from pageObjects.dashboard import DashboardPage
from pytest_bdd import given, scenarios, when, then, scenario, parsers

scenarios("../features/orderTransaction.feature")

@pytest.fixture
def shared_data():
    return {}

@given(parsers.parse("place the item order with user credentials {username} and {password}"))
def step_impl(context, playwright, username, password):
    apiUtils = APIUtils()
    context.orderId = apiUtils.createOrder(playwright, {"userEmail": username, "userPassword": password})

@given("the user is on login page")
def step_impl(context, shared_data, browser_instance):
    loginPage = LoginPage(browser_instance) 
    loginPage.navigate()
    shared_data["loginPage"] = loginPage
    
@when(parsers.parse("when I login with username {username} and password {password}"))
def step_impl(context, shared_data, username, password):
    loginPage = shared_data["loginPage"]
    dashboardPage = loginPage.login({"userEmail": username, "userPassword": password})
    shared_data["dashboardPage"] = dashboardPage
    
@when("navigate to orders page")
def step_impl(context, shared_data):
    dashboardPage = shared_data["dashboardPage"]
    dashboardPage.goToOrders()
    
@when("select the order id")
def step_impl(context, shared_data):
    orderHistoryPage = shared_data["dashboardPage"].goToOrders()
    orderDetailsPage = orderHistoryPage.selectOrder(context.orderId)
    shared_data["orderDetailsPage"] = orderDetailsPage

@then("order message is successfully shown in details page")
def step_impl(context, shared_data):
    orderDetailsPage = shared_data["orderDetailsPage"]
    orderDetailsPage.verifyOrderMessage()
