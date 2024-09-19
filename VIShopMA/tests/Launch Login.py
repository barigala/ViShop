from time import sleep
import allure
import self
from appium.webdriver.common.appiumby import AppiumBy

from VIShopMA.base.DriverClass import Driver
from VIShopMA.base.basepage import BasePage
import VIShopMA.utils.customLogger as cl

driver1 = Driver()
log = cl.customLogger()

driver = driver1.getDriverMethod()
log.info("Launch App")

bp = BasePage(driver)

"""
bp.clickElement('enter mobile number', 'text')
bp.screenShot('Launch Page')
bp.clickElement('NONE OF THE ABOVE', 'text')
bp.screenShot('Input Mobile Number')
bp.sendNumberViaKeypad('7796148513')
bp.screenShot('After Input Mobile Number')
sleep(2)
bp.clickElement('//android.widget.TextView[@text="send OTP"]','xpath')
bp.screenShot('Send OTP Page')
sleep(2)
bp.waitForElement('login with OTP','text')
bp.sendOtpViaKeypad('1234')
bp.screenShot('After Input OTP')
sleep(5)
bp.clickElement('login with OTP', 'text')
bp.screenShot('Login with OTP Page')
print("Test completed successfully")
sleep(30)
print("Test completed successfully")
sleep(30)
print("Test completed successfully")
bp.clearRecentApps()
bp.relaunchApp('com.mventus.selfcare.activity', 'com.mventus.selfcare.activity.MainActivity')
"""

bp.waitAndPerformAction('click','shop','text')
bp.screenShot('Navigate to shop')
bp.clickElement('deals', 'text')
bp.screenShot('Navigate to deals')
bp.clickElement('explore','text')
bp.screenShot('Navigate to explore')
bp.clickElement('my orders', 'text')
bp.screenShot('Navigate to my orders')
bp.clickElement('shop','text')
bp.clickElement('//android.view.ViewGroup[@content-desc="DS_SHOPshop-account-icon.webp"]','xpath')
bp.screenShot('Navigate to account')
bp.clickElement('your orders', 'text')
bp.pressBackButton()




sleep(10)
driver.quit()
print("Test completed successfully")