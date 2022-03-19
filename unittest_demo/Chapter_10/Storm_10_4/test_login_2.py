from selenium import webdriver
import unittest
from parameterized import parameterized, param


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        # 访问登录页
        self.driver.get('http://localhost:81/redmine/login')

    '''
    1、@parameterized.expand()，括号中传递列表；
    2、列表中传递元组，每个元组代表一个测试用例；
    3、每个测试用例包含了3个参数：
        1）第一个是用户名的取值；
        2）第二个是密码的取值；
        3）第三个是登录成功与否：我们约定0代码登录失败，1代表成功；
    '''
    @parameterized.expand([('admin', 'error', '0'),('admin', 'rootroot', '1')])
    def test_001_login(self, username, password, status):
        # 登录名
        login_name = self.driver.find_element_by_id('username')
        login_name.clear()
        login_name.send_keys(username)
        # 登录密码
        login_pwd = self.driver.find_element_by_id('password')
        login_pwd.clear()
        login_pwd.send_keys(password)
        # 登录按钮
        login_btn = self.driver.find_element_by_id('login-submit')
        login_btn.click()
        if status == '0':
            # 登录失败后的提示信息
            ele = self.driver.find_element_by_id('flash_error')
            self.assertIn('无效的用户名或密码', self.driver.page_source)
        elif status == '1':
            # 登录后显示的用户名
            name = self.driver.find_element_by_link_text(username)
            self.assertEqual(name.text, username)
        else:
            print('参数化的状态只能传入0或1')


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()