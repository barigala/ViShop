# 1. Import the files
import  unittest
from VIShopMA.tests.AccountPageTest import AccountPageTest

# 2. Create the object of the class using unitTest
ap_tests = unittest.TestLoader().loadTestsFromTestCase(AccountPageTest)

# 3. Create TestSuite
sanityTest = unittest.TestSuite([ap_tests])

# 4. Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(sanityTest)

