import unittest
from selenium import webdriver
from Chapter_12.Storm_12_1.PageObject.redmine_operations import *
from parameterized import parameterized, param

'''
测试用例：验证登录功能
'''

url = "http://localhost:81/redmine/login"

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(url)

    @parameterized.expand([('admin', 'error', '0'), ('admin', 'rootroot', '1')])
    def test_login(self, username, password, status):
        LoginPage(self.driver).enter_username(username)
        LoginPage(self.driver).enter_password(password)
        LoginPage(self.driver).click_login_button()
        if status == '0':
            # 登录失败后的提示信息
            text = LoginPage(self.driver).find_login_failed_info().text
            self.assertEqual(text, '无效的用户名或密码')
        elif status == '1':
            # 登录后显示的用户名
            name = LoginPage(self.driver).find_login_name().text
            self.assertIn(username, name)
        else:
            print('参数化的状态只能传入0或1')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()