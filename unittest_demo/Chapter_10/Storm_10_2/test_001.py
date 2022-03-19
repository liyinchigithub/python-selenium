import unittest


class MyTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_aaa(self):
        print('aaa')
        self.assertEqual('a','a')

    def test_bbb(self):
        print('bbb')
        self.assertEqual('b','b')

if __name__ == '__main__':
    unittest.main()