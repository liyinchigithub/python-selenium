import unittest


class TestStorm(unittest.TestCase):
    def setUp(self):
        print('setUp')

    def test_first(self):
        self.assertEqual('storm', 'storm')

    def tearDown(self):
        print('tearDown')


if __name__ == '__main__':
    unittest.main()