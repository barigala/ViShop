from VIShopMA.base.DriverClass import Driver
from VIShopMA.base.basepage import BasePage
import VIShopMA.utils.customLogger as cl

driver1 = Driver()
log = cl.customLogger()

driver = driver1.getDriverMethod()
log.info("Launch App")

bp = BasePage(driver)
element = bp.waitForElement('enter mobile number', 'text')
element.click()


