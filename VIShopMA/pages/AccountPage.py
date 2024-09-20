from VIShopMA.base.basepage import BasePage
import VIShopMA.utils.customLogger as cl


class accountpage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact us form
    _accountButton = '//android.view.ViewGroup[@content-desc="DS_SHOPshop-account-icon.webp"]'  # xpath
    _pagetitle = "account"  # text
    _yourorders = "your orders"  # text
    _cc = "credit cards"  # text
    _coupons = "coupons"  # text
    _savedpay = '//android.widget.TextView[@text="saved payments"]'  # xpath

    def ClickaccountButton(self):
        self.clickElement(self._accountButton, "xpath")
        cl.allureLogs("Clicked on Account Button")

    def verifyPagetitle(self):
        element = self.isDisplayed(self._pagetitle, "text")
        assert element == True
        cl.allureLogs("Verified on Account Page Title")

    def NavOrders(self):
        self.clickElement(self._yourorders,"text")
        cl.allureLogs("Clicked on My Orders")

    def NavCC(self):
        self.clickElement(self._cc,"text")
        cl.allureLogs("Clicked on Credit Cards")

    def NavCoupons(self):
        self.clickElement(self._coupons,"text")
        cl.allureLogs("Clicked on Coupons")

    def NavSavdPay(self):
        self.clickElement(self._savedpay,"xpath")
        cl.allureLogs("Clicked on Saved Payments")

