import unittest
import pytest
from driver import driver

from VIShopMA.pages.AccountPage import accountpage
import VIShopMA.utils.customLogger as cl

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class AccountPageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        ap = accountpage()

    @pytest.mark.run(order=1)
    def test_NavtoAccountPage(ap=None):
        cl.allureLogs("Navigated to account page")
        ap.ClickaccountButton()
        ap.verifyPagetitle()
        ap.NavCC()
        driver.press_keycode(4)  # Keycode for the BACK button
        ap.NavCoupons()



"""
bp.waitAndPerformAction('click','shop','text')
ap.ClickaccountButton()
ap.verifyPagetitle()
ap.NavOrders()
bp.pressBackButton()
ap.NavCC()
bp.pressBackButton()
ap.NavCoupons()
bp.pressBackButton()
ap.NavSavdPay()
"""