import re
import time

import allure
import self
from allure_commons.types import AttachmentType
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import VIShopMA.utils.customLogger as cl
from appium import webdriver

class BasePage:
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver


    def waitForElement(self, locatorValue, locatorType):
        locatorType = locatorType.lower()
        element = None
        wait = WebDriverWait(self.driver,25,poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])

        if locatorType == "id":
            element = wait.until(lambda x:x.find_element(AppiumBy.ID, locatorValue))
            return element
        elif locatorType == "class":
            element = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, locatorValue))
            return element
        elif locatorType == "des":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().description("%s")'%(locatorValue)))
            return element
        elif locatorType == "index":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().index({int(locatorValue)})'))
            return element
        elif locatorType == "text":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("%s")' % (locatorValue)))
            return element
        elif locatorType == "xpath":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.XPATH, '%s' % (locatorValue)))
            return element
        else:
            self.log.info("Locator Value" + locatorValue + "not found")

        return element



    def getElement(self, locatorValue,locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element=self.waitForElement(locatorValue,locatorType)
            self.log.info("Element found with LocatoryType" + locatorType + " with the locatorValue:" + locatorValue)
        except:
            self.log.info("Element not found with LocatoryType" + locatorType + " and with the locatorValue:" + locatorValue)
        return element

    def clickElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element=self.waitForElement(locatorValue,locatorType)
            element.click()
            self.log.info("Clicked on Element with LocatoryType" + locatorType + " with the locatorValue:" + locatorValue)
        except:
            self.log.info("Unable to click on Element with LocatoryType" + locatorType + " and with the locatorValue:" + locatorValue)
            self.takeScreenshot(locatorType)
            assert False

    def sendText(self,text, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element=self.waitForElement(locatorValue,locatorType)
            element.send_keys(text)
            self.log.info("Send text on Element with LocatoryType" + locatorType + " with the locatorValue:" + locatorValue)
        except:
            self.log.info("Element not found with LocatoryType" + locatorType + " and with the locatorValue:" + locatorValue)
            self.takeScreenshot(locatorType)
            assert False

    def isDisplayed(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element=self.waitForElement(locatorValue,locatorType)
            element.is_displayed()
            self.log.info("Element with LocatoryType" + locatorType + " with the locatorValue:" + locatorValue+"is displayed")
            return True
        except:
            self.log.info("Element not found with LocatoryType" + locatorValue + " and with the locatorValue:" + locatorType + "is not displayed")
            self.takeScreenshot(locatorType)
            return False

    def clickKeypadButton(self, digit):
        try:
            locatorType = "xpath"
            locatorValue = f'//android.widget.TextView[@text="{digit}"]'
            element = self.getElement(locatorValue, locatorType)
            element.click()
            time.sleep(1)
            self.log.info(f"Clicked on keypad button with digit '{digit}' using XPATH locator.")
        except Exception as e:
            self.log.error(
                f"Failed to click on keypad button with digit '{digit}' using XPATH locator. Error: {str(e)}")

    def sendNumberViaKeypad(self, number):
        try:
            previous_digit = None
            for digit in str(number):
                if previous_digit == digit:
                    time.sleep(1)
                    self.log.info(f"Added a delay for consecutive identical digit '{digit}'")

                self.clickKeypadButton(digit)

                previous_digit = digit

            self.log.info(f"Successfully sent the number '{number}' via keypad.")
        except Exception as e:
            self.log.error(f"Failed to send the number '{number}' via keypad. Error: {str(e)}")


    def clickOtpButton(self, digit):
        try:
            locatorType = "xpath"
            # Use the constant '[2]' part in the XPATH as requested
            locatorValue = f'(//android.widget.TextView[@text="{digit}"])[2]'
            element = self.getElement(locatorValue, locatorType)
            element.click()
            self.log.info(f"Clicked on OTP button with digit '{digit}' using XPATH locator '{locatorValue}'.")
        except Exception as e:
            self.log.error(f"Failed to click on OTP button with digit '{digit}' using XPATH locator. Error: {str(e)}")

    def sendOtpViaKeypad(self, otp):
        try:
            previous_digit = None
            for digit in str(otp):
                if previous_digit == digit:
                    # Add a short delay to handle consecutive identical digits
                    time.sleep(0.5)
                    self.log.info(f"Added a delay for consecutive identical digit '{digit}' in OTP.")
                self.clickOtpButton(digit)
                previous_digit = digit  # Update the previous digit to track repetition

            self.log.info(f"Successfully sent the OTP '{otp}' via keypad.")
        except Exception as e:
            self.log.error(f"Failed to send the OTP '{otp}' via keypad. Error: {str(e)}")

    def clearRecentApps(self):
            # Wait for the loading to happen
            time.sleep(2)
            self.driver.background_app(2)  # Minimizes the app for some time
            self.log.info("App minimized successfully before relaunching.")

            # Open the recent apps screen
            self.driver.press_keycode(187)  # 187 is the keycode for recent apps
            self.log.info("Pressed the recent apps keycode (187).")

            time.sleep(2)

            # Attempt to find and click the 'Clear all' button
            element = self.waitForElement('com.mi.android.globallauncher:id/clearAnimView', 'id')
            element.click()
            self.log.info("Clicked on 'Clear all' button to close recent apps.")
            #if element:
            #   element.click()
            #    self.log.info("Clicked on 'Clear all' button to close recent apps.")
            #else:
            #    self.log.error("Clear all button not found on recent apps screen.")

            # Wait to ensure recent apps are cleared
            time.sleep(2)
            self.driver.background_app(2)  # Minimizes the app for some time


    def relaunchApp(self, appPackage, appActivity):
        try:
            self.driver.background_app(2)
            # Relaunch the app using the provided package and activity
        #    self.driver.start_activity(appPackage, appActivity)
            self.driver.launchapp(appPackage, appActivity)
            self.log.info(f"App relaunched with package: {appPackage}, activity: {appActivity}")

        except Exception as e:
            self.log.error(
                f"Failed to relaunch the app with package: {appPackage} and activity: {appActivity}. Error: {str(e)}")

    def waitAndPerformAction(self, action, locatorValue, locatorType="id", text=None):
        """
        Combines actions to wait for an element and perform a click, send text, or return the element.

        :param action: The action to perform: "click", "sendtext", or "get"
        :param locatorValue: The locator value for the element (e.g., element ID, xpath)
        :param locatorType: The locator type for the element ("id", "xpath", "class", etc.)
        :param text: The text to send if action is "sendtext"
        :return: Element if action is "get", otherwise None
        """
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)

            if action == "click":
                element.click()
                self.log.info(f"Clicked on element with locatorType '{locatorType}' and locatorValue '{locatorValue}'")

            elif action == "sendtext":
                if text is not None:
                    element.send_keys(text)
                    self.log.info(
                        f"Sent text '{text}' to element with locatorType '{locatorType}' and locatorValue '{locatorValue}'")
                else:
                    self.log.info("No text provided to send.")

            elif action == "get":
                self.log.info(f"Retrieved element with locatorType '{locatorType}' and locatorValue '{locatorValue}'")
                return element

            else:
                self.log.info(f"Unknown action '{action}' provided.")

        except Exception as e:
            self.log.info(
                f"Failed to perform '{action}' on element with locatorType '{locatorType}' and locatorValue '{locatorValue}'. Error: {e}")

        return None if action != "get" else element

    def screenShot(self, screenshotName):
        filename = screenshotName + "_"+(time.strftime("%d_%m_%Y_%H_%M_%S"))+".png"
        screenshotDirectory = "../screenshot/"
        screenshotPath = screenshotDirectory + filename
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("Screenshot saved at: " + screenshotPath)
        except:
            self.log.info("Unable to save screenshot to the path: "+ screenshotPath)


    def pressHomeButton(driver):
        driver.press_keycode(3)  # Keycode for the HOME button

    def pressBackButton(self):
        """
        Press the BACK button on the Android device.
        """
        try:
            self.driver.press_keycode(4)  # Keycode for the BACK button
            self.log.info("Pressed BACK button")
        except Exception as e:
            self.log.error(f"Error pressing BACK button: {str(e)}")


    #def takeScreenshot(self,text):
    #    allure.attach(self.driver.get_screenshot_as_png(text),name=text, attachment_type=AttachmentType.PNG)

    def takeScreenshot(self, description):
        try:
            screenshot = self.driver.get_screenshot_as_png()  # Get the screenshot as PNG
            allure.attach(screenshot, name=description, attachment_type=AttachmentType.PNG)
            self.log.info(f"Screenshot taken and attached to Allure: {description}")
        except Exception as e:
            self.log.error(f"Failed to take screenshot: {str(e)}")