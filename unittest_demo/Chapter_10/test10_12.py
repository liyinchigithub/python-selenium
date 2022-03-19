import unittest
import sys


'''
满足条件跳过
'''
class MyTest(unittest.TestCase):
    a = 4
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_aaa(self):
        print('aaa')

    @unittest.skipIf(a>3, 'info')
    def test_ddd(self):
        print('ddd')


    def test_ccc(self):
        print('ccc')

    def test_bbb(self):
        print('bbb')

if __name__ == '__main__':
    unittest.main()