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
        self.driver = request.cls.driver  # Using class-level driver from beforeClass fixture in the test case class.  # This is a workaround for the lack of pytest fixture scope control.  # Normally, you'd use a fixture to provide the driver to each test method.  # However, since we're using autouse=True, the driver will be provided to the test class itself, not to each test method.  # This allows us to share the
        self.ap = accountpage(self.driver)

    @pytest.mark.run(order=1)
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

