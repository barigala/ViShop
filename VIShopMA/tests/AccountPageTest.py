import unittest
import pytest
import self
from appium import webdriver
from VIShopMA.pages.AccountPage import accountpage
import VIShopMA.utils.customLogger as cl

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class AccountPageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self, request):
        self.ap = accountpage(self.driver)

    @pytest.mark.run(order=7)
    def test_NavtoAccountPage(self):
        cl.allureLogs("Navigated to account page")
        self.ap.ClickaccountButton()
        self.ap.verifyPagetitle()
        self.ap.NavCC()
        self.driver.press_keycode(4)  # Keycode for the BACK button
        self.ap.NavCoupons()
        self.driver.press_keycode(4)  # Keycode for the BACK button
        self.ap.NavOrders()
        self.driver.press_keycode(4)  # Keycode for the BACK button
        self.ap.NavSavdPay()

