import unittest


'''
@unittest.skip('skip info')，无条件跳过
'''
class MyTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @unittest.skip('skip info')
    def test_aaa(self):
        print('aaa')

    def test_ddd(self):
        print('ddd')

    def test_ccc(self):
        print('ccc')

    def test_bbb(self):
        print('bbb')

if __name__ == '__main__':
    unittest.main()