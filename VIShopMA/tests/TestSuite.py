# 1. Import the files
import  unittest
from VIShopMA.tests.AccountPageTest import AccountPageTest
from VIShopMA.tests.LoginPageTest import LoginPageTest

# 2. Create the object of the class using unitTest
lp_tests = unittest.TestLoader().loadTestsFromTestCase(LoginPageTest)
ap_tests = unittest.TestLoader().loadTestsFromTestCase(AccountPageTest)

# 3. Create TestSuite
sanityTest = unittest.TestSuite([lp_tests, ap_tests])

# 4. Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(sanityTest)

