import unittest


first = 20
class TestStorm(unittest.TestCase):
    def setUp(self):  # 在每个测试用例执行前执行一次
        print('setUp')

    def test_age(self):  # 用例名小写字母，以test开头
        second = first + 5  # 用例操作
        self.assertEqual(second, 25) # 操作结果断言

    def tearDown(self): # 在每个测试用例后执行一次
        print('tearDown')


if __name__ == '__main__':
    unittest.main()