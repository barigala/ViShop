import unittest
import pytest
import self
from appium import webdriver
from VIShopMA.pages.LoginPage import loginpage
import VIShopMA.utils.customLogger as cl

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class LoginPageTest(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classObjects(self, request):
        self.login_page = loginpage(self.driver)

    @pytest.mark.run(order=1)
    def test_NavtillInputMobileNumber(self):
        print("Now running test_NavtillInputMobileNumber")
        cl.allureLogs("Navigating to Mobile Number Input Field")
        self.login_page.ClickNumberInputField()
        self.login_page.ClickDialogBox()
        cl.allureLogs("Navigation to Mobile Number Input Field test completed successfully")

    @pytest.mark.run(order=2)
    def test_InputMobileNumber(self):
        print("Now running test_InputMobileNumber")
        cl.allureLogs("Navigating to Mobile Number Input Field")
        valid_mobile_number = "7507233095"
        self.login_page.inputValidMobileNumber(valid_mobile_number)
        cl.allureLogs("Mobile number input test completed successfully")

    @pytest.mark.run(order=3)
    def test_clickOTP(self):
        print("Now running test_clickOTP")
        cl.allureLogs("Input OTP")
        self.login_page.ClickOTPButton()

    @pytest.mark.run(order=4)
    def test_inputOTP(self):
        print("Now running input OTP")
        cl.allureLogs("Input OTP")
        valid_mobile_number = "1234"
        self.login_page.inputOTP(valid_mobile_number)
        cl.allureLogs("OTP number input test completed successfully")

    @pytest.mark.run(order=5)
    def test_LoginWOTP(self):
        print("Now running test_clickOTP Button")
        cl.allureLogs("Click login OTP Button")
        self.login_page.LoginWOTPButton()

    @pytest.mark.run(order=6)
    def test_Shop(self):
        print("Now running test_Shop Navigation")
        cl.allureLogs("Click Shop Button")
        self.login_page.NavtoShop()