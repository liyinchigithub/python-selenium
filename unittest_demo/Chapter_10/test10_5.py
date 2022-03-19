import unittest

'''
演示如何通过TestLoader()来构造TestSuite
'''

class TestFrist(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_one(self):
        print('1')
        self.assertEqual(1,1)

    def test_two(self):
        print('2')
        self.assertEqual(2,2)

class TestSecond(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_three(self):
        print('3')
        self.assertEqual(3,3)

    def test_four(self):
        print('4')
        self.assertEqual(4,4)

if __name__ == '__main__':
    testcase2 = unittest.TestLoader().loadTestsFromTestCase(TestSecond)
    suite = unittest.TestSuite([testcase2])
    unittest.TextTestRunner().run(suite)