import unittest


class MyTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_aaa(self):
        print('aaa')

    def test_bbb(self):
        print('bbb')

if __name__ == '__main__':
    unittest.main()
