import unittest


class MyTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ddd(self):
        print('ddd')

    def test_ccc(self):
        print('ccc')


if __name__ == '__main__':
    unittest.main()
