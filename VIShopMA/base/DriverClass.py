from appium import webdriver
from appium.options.android import UiAutomator2Options

class Driver:

    def getDriverMethod(self):
        # Desired capabilities for the app
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.automation_name = 'UiAutomator2'
        options.platform_version = '14'
        options.device_name = 'POCO X6 5G'
        options.udid = '79003d15'
        options.app = 'D:\\PyProjects\\Vi_Release_50_10-Sept-24.apk'
        options.app_package = 'com.mventus.selfcare.activity'
        options.app_activity = 'com.mventus.selfcare.activity.MainActivity'

        # Initialize the Appium driver
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)
        return driver
