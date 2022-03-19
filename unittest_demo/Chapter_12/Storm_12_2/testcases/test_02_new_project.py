from selenium import webdriver
import time, pytest
from Chapter_12.Storm_12_2.pageobject import login_page, project_new_page, project_list_page


# 通过时间戳，构造唯一project name
project_name = 'project_{}'.format(time.time())
username = 'admin'
password = 'rootroot'

class TestNewProject():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        # 访问登录页
        self.driver.get('http://localhost:81/redmine/login')
        # 登录
        login_page.LoginScenario(self.driver).login(username, password)

    def test_new_project(self):
        # 访问项目列表页
        self.driver.get('http://localhost:81/redmine/projects')
        # 新建项目按钮
        project_list_page.ProjectListOper(self.driver).click_new_pro_btn()
        project_new_page.ProjectNewScenario(self.driver).new_project(project_name)
        # 新建项目成功后的提示信息
        text = project_new_page.ProjectNewOper(self.driver).get_pro_commit_info()
        assert text == '创建成功'

    def teardown(self):
        self.driver.quit()

if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', '../report/'])