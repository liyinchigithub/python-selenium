import unittest


class MyTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ddd(self):
        print('ddd')
        self.assertEqual('d','d')

    def test_ccc(self):
        print('ccc')
        self.assertEqual('c','c')


if __name__ == '__main__':
    unittest.main()