from selenium import webdriver
import pytest


data = [['admin', 'error', '0'], ['admin', 'rootroot', '1']]
@pytest.mark.parametrize(("username", "password", "status"), data)
class TestLogin():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        # 访问登录页
        self.driver.get('http://localhost:81/redmine/login')

    def teardown(self):
        self.driver.quit()

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
            assert '无效的用户名或密码' in self.driver.page_source
        elif status == '1':
            # 登录后显示的用户名
            name = self.driver.find_element_by_link_text(username)
            assert name.text == username
        else:
            print('参数化的状态只能传入0或1')

if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/'])