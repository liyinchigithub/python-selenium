from selenium import webdriver
import unittest,time

class VisitPTPress(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_open_ptpress(self):
        self.driver.get('https://www.ptpress.com.cn/') # 打开人民邮电出版社官网
        self.assertIn('图书', self.driver.page_source) # 断言：网页中有“图书”字样

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()