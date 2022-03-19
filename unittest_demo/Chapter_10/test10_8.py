import unittest

if __name__ == '__main__':
    testSuite = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=2).run(testSuite)