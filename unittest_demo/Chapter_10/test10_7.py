import unittest
from Chapter_10 import test10_5

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(test10_5.TestFrist("test_one"))
    suite.addTest(test10_5.TestSecond("test_four"))
    unittest.TextTestRunner().run(suite)