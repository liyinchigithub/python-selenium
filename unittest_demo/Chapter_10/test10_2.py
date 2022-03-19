import unittest


class TestStorm(unittest.TestCase):
    @classmethod # 注意，必须有该装饰器
    def setUpClass(cls): # 在整个class开始前执行一次
        print('setUpClass')

    def setUp(self):  # 在每个测试用例执行前执行一次
        print('setUp')

    def test_first(self):  # 第一条测试用例
        print('first')
        self.assertEqual('first', 'first')

    def test_second(self): # 第二条测试用例
        print('second')
        self.assertEqual('second', 'second')

    def tearDown(self): # 在每个测试用例后执行一次
        print('tearDown')

    @classmethod
    def tearDownClass(cls): # 在整个class执行最后执行一次
        print('tearDownClass')


if __name__ == '__main__':
    unittest.main()