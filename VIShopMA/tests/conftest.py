import os
import shutil

import pytest
import time

from setuptools.compat.py311 import shutil_rmtree

from VIShopMA.base.DriverClass import Driver


ALLURE_RESULTS_PATH = 'D:\PyProjects\ViShop\VIShopMA\reports\allurereports'

@pytest.fixture(scope='class')
def beforeClass(request):
    # Clean up Allure logs before the test run

    print('Cleaning Allure logs...')
    if os.path.exists(ALLURE_RESULTS_PATH):
        # Delete all files in the directory without removing the folder itself
        for filename in os.listdir(ALLURE_RESULTS_PATH):
            file_path = os.path.join(ALLURE_RESULTS_PATH, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)  # Remove the file
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # Remove subdirectories, if any
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')

    print('Before Class')
    driver1 = Driver()
    driver = driver1.getDriverMethod()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print('After Class')

@pytest.fixture()
def beforeMethod():
    print('Before Method')
    yield
    print('After Method')