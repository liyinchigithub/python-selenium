from selenium import webdriver
import unittest


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        # 访问登录页
        self.driver.get('http://localhost:81/redmine/login')

    def test_001_login_err(self):
        # 用例一：错误的密码登录失败
        # 登录名
        login_name = self.driver.find_element_by_id('username')
        login_name.clear()
        login_name.send_keys('admin')
        # 登录密码
        login_pwd = self.driver.find_element_by_id('password')
        login_pwd.clear()
        login_pwd.send_keys('error')
        # 登录按钮
        login_btn = self.driver.find_element_by_id('login-submit')
        login_btn.click()
        # 登录失败后的提示信息
        ele = self.driver.find_element_by_id('flash_error')
        self.assertIn('无效的用户名或密码', self.driver.page_source)

    def test_002_login_suc(self):
        # 用例二：正确的密码登录成功
        # 登录名
        login_name = self.driver.find_element_by_id('username')
        login_name.clear()
        login_name.send_keys('admin')
        # 登录密码
        login_pwd = self.driver.find_element_by_id('password')
        login_pwd.clear()
        login_pwd.send_keys('rootroot')
        # 登录按钮
        login_btn = self.driver.find_element_by_id('login-submit')
        login_btn.click()
        # 登录后显示的用户名
        name = self.driver.find_element_by_link_text('admin')
        self.assertEqual(name.text, 'admin')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()