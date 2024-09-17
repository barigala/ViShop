import allure
from VIShopMA.base.DriverClass import Driver
from VIShopMA.base.basepage import BasePage
import VIShopMA.utils.customLogger as cl

driver1 = Driver()
log = cl.customLogger()

driver = driver1.getDriverMethod()
log.info("Launch App")

bp = BasePage(driver)
bp.waitForElement('enter mobile number', 'text').click()

# Adding a screenshot using Allure
#allure.attach(bp.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)

# Adding a step to Allure report    the screenshot
#cl.allureLogs("User enters mobile number")

bp.waitForElement('NONE OF THE ABOVE', 'text').click()

# Adding a step to Allure report
#cl.allureLogs("User cancels the number entry")

driver.quit()

print("Test completed successfully")