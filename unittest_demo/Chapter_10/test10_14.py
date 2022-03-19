import unittest


class TestMath(unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_001(self):
        j = 5
        self.assertEqual(j + 1, 6) # 判断相等
        self.assertNotEqual(j + 1, 5) # 判断不相等

    def test_002(self):
        j = True
        f = False
        self.assertTrue(j) # 判断j是否为True
        self.assertFalse(f) # 判断f是否为False

    def test_003(self):
        j = 'Storm'
        self.assertIs(j, 'Storm') # 判断j是否是“Storm”
        self.assertIsNot(j, 'storm') # 判断j是否是“storm”，区分大小写

    def test_004(self):
        j = None
        t = 'Storm'
        self.assertIsNone(j)  # 判断j是否为None
        self.assertIsNotNone(t) # 判断t是否不是None

    def test_005(self):
        j = 'Storm'
        self.assertIn(j, 'Storm')  # 判断j包含在“Storm”中
        self.assertNotIn(j, 'xxx')  # 判断j是否没有包含在“xxx”中

    def test_006(self):
        j = 'Storm'
        self.assertIsInstance(j, str) # 判断j的类型是str
        self.assertNotIsInstance(j, int) # 判断j的类型不是int

    def tearDown(self):
        print("test end")

if __name__ == '__main__':
    unittest.main()