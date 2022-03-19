from selenium import webdriver
import pytest
# 导入本用例用到的页面对象文件
from Chapter_13.Test.PageObject import login_page
from Chapter_13.Common.parse_csv import parse_csv
from Chapter_13.Common.parse_yml import parse_yml

host = parse_yml("../../Config/redmine.yml", "websites", "host")
# host = parse_yml("D:\Love\Chapter_13\Config\\redmine.yml", "websites", "host")
url = "http://"+host+"/redmine/login"
data = parse_csv("../../Data/test_01_login.csv")
# data = parse_csv("D:\Love\Chapter_13\Data\\test_01_login.csv")
# print(data)
# data = [('admin', 'error', '0'), ('admin', 'rootroot', '1')]
@pytest.mark.parametrize(("username", "password", "status"), data)
class TestLogin():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.driver.implicitly_wait(20)
        # 访问登录页
        self.driver.get(url)


    def teardown(self):
        self.driver.quit()

    def test_001_login(self, username, password, status):
        # 登录的3个操作用业务场景方法一条语句代替
        login_page.LoginScenario(self.driver).login(username,password)
        if status == '0':
            # 登录失败后的提示信息，通过封装的元素操作来代替
            text = login_page.LoginOper(self.driver).get_login_failed_info()
            assert  text == '无效的用户名或密码'
        elif status == '1':
            # 登录后显示的用户名，通过封装的元素操作来代替
            text = login_page.LoginOper(self.driver).get_login_name()
            assert username in text
            # 增加一个断言
            assert "我的工作台" in self.driver.page_source
        else:
            print('参数化的状态只能传入0或1')

if __name__ == '__main__':
    # pytest.main(['-s', '-q', '--alluredir', '../report/'])
    # pytest.main(['-s', 'test_01_login.py'])
    pytest.main(['-s', '-q', '--alluredir', '../../Report/report'])