import unittest

'''
演示如何通过TestLoader()来构造TestSuite
'''

class TestFrist(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_001_one(self):
        print('1')
        self.assertEqual(1,1)

    def test_002_two(self):
        print('2')
        self.assertEqual(2,2)

class TestSecond(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_003_three(self):
        print('3')
        self.assertEqual(3,3)

    def test_004_four(self):
        print('4')
        self.assertEqual(4,4)

if __name__ == '__main__':
    unittest.main()