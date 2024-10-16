from behave import given, when, then
from VIShopMA.pages.AccountPage import accountpage
from VIShopMA.base.DriverClass import Driver

'''
@given('I launch the app')
def launch_app(context):
    driver_instance = Driver()
    context.driver = driver_instance.getDriverMethod()
    context.account_page = accountpage(context.driver)
'''

@given('I see Account Button')
def verifyAccountButton(context):
    assert context.accountpage.isAccountButtonDisplayed()

@when('I click on the Account button')
def ClickaccountButton(context):
    context.accountpage.ClickaccountButton()

@then('I should see the Account page title')
def verifyPagetitle(context):
    context.accountpage.verifyPagetitle()

@when('I navigate to "{section}"')
def navigate_to_section(context, section):
    if section == "Credit Cards":
        context.accountpage.NavCC()
    elif section == "Coupons":
        context.accountpage.NavCoupons()
    elif section == "Orders":
        context.accountpage.NavOrders()
    elif section == "Saved Payments":
        context.accountpage.NavSavdPay()

@then('I should return to the Account page')
def pressbackbutton(context):
    context.driver.press_keycode(4)
