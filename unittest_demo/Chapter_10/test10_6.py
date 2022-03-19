import unittest
from Chapter_10 import test10_5

if __name__ == '__main__':
    testcase2 = unittest.TestLoader().loadTestsFromTestCase(test10_5.TestSecond)
    suite = unittest.TestSuite([testcase2])
    unittest.TextTestRunner().run(suite)