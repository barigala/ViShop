import pytest
from pytest_bdd import scenarios, given, when, then
from VIShopMA.pages.AccountPage import accountpage

scenarios('../features/accountpage.feature')

@pytest.fixture
def account_page(driver):
    return accountpage(driver)

@given('the app is launched')
def app_launched():
    # Add any preconditions or app launch verification if needed
    pass

@when('the user clicks the account button')
def click_account_button(account_page):
    account_page.ClickaccountButton()

@then('the account page should be displayed')
def verify_account_page_displayed(account_page):
    # Assuming you have a method to verify that the account page is displayed
    assert account_page.isAccountPageDisplayed()
