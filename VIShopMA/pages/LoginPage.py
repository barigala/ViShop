import time
from os import times
from time import sleep
from VIShopMA.base.basepage import BasePage
import VIShopMA.utils.customLogger as cl


class loginpage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact us form
    _numberInputField = 'enter mobile number'  # text
    _numberDialogBox = "NONE OF THE ABOVE"  # text
    _sendOTP = "send OTP"  # text
    _inputOTP = "login with OTP"  # text
    _shopButton = "shop"  # text


    def ClickNumberInputField(self):
        self.clickElement(self._numberInputField, "text")
        cl.allureLogs("Clicked on Mobile Number Input Field")
        self.screenShot("Clicked on Mobile Number Input Field")

    def ClickDialogBox(self):
        self.clickElement(self._numberDialogBox, "text")
        cl.allureLogs("Clicked on Dialog Box")
        self.screenShot("Clicked on Dialog Box")

    def inputValidMobileNumber(self, mobile_number):
        """
        This method validates the mobile number length and inputs the 10-digit mobile number using the sendNumberViaKeypad method.
        """
        if len(mobile_number) == 10 and mobile_number.isdigit():
            cl.allureLogs(f"Entering 10-digit mobile number: {mobile_number}")

            for digit in mobile_number:
                self.sendNumberViaKeypad(digit)
                cl.allureLogs(f"Entered digit: {digit}")
                time.sleep(0.5)  # Optional: Delay to ensure stability between digit inputs

            cl.allureLogs("Mobile number input completed")
            self.screenShot("Entered Mobile Number")
        else:
            cl.allureLogs(f"Invalid mobile number: {mobile_number}. Please enter a valid 10-digit number.")
            raise ValueError("Mobile number must be exactly 10 digits and numeric.")

    def ClickOTPButton(self):
        self.clickElement(self._sendOTP, "text")
        cl.allureLogs("Clicked on OTP button")
        self.screenShot("Clicked on OTP button")

    def inputOTP(self, OTP_number):
        """
        This method validates the mobile number length and inputs the 10-digit mobile number using the sendNumberViaKeypad method.
        """
        if len(OTP_number) == 4 and OTP_number.isdigit():
            cl.allureLogs(f"Entering 4-digit OTP number: {OTP_number}")

            for digit in OTP_number:
                self.sendOtpViaKeypad(digit)
                cl.allureLogs(f"Entered digit: {digit}")
                time.sleep(0.5)  # Optional: Delay to ensure stability between digit inputs

            cl.allureLogs("OTP number input completed")
            self.screenShot("Entered OTP Number")
        else:
            cl.allureLogs(f"Invalid mobile number: {OTP_number}. Please enter a valid 4-digit number.")
            raise ValueError("Mobile number must be exactly 4 digits and numeric.")

    def LoginWOTPButton(self):
        self.clickElement(self._inputOTP, "text")
        cl.allureLogs("Clicked on Login with OTP button")
        self.screenShot("Clicked on Login with OTP button")

    def NavtoShop(self):
        self.waitForElement(self._shopButton, "text")
        time.sleep(0.5)
        self.clickElement(self._shopButton, "text")
        cl.allureLogs("Clicked on Shop button")
        self.screenShot("Clicked on Shop button")