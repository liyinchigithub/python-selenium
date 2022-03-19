import unittest
import time
from Chapter_12.Storm_12_1.Scenario import redmine_login,redmine_new_project
from Chapter_12.Storm_12_1.PageObject.redmine_operations import *


'''
验证新建项目
'''
class AddProjectTest(unittest.TestCase):
    def setUp(self):
        # 登录，并访问新建项目列表页
        self.driver = redmine_login.LoginScenario().redmine_login()
        self.driver.get('http://localhost:81/redmine/projects')

    def test_add_project(self):
        # 新建项目按钮
        _project_name = 'project_{}'.format(time.time())
        ProjectListPage(self.driver).click_new_pro_btn()
        NewProjectPage(self.driver).enter_projectname(_project_name)
        NewProjectPage(self.driver).click_com_btn()
        text = NewProjectPage(self.driver).get_pro_commit_info().text
        self.assertEqual(text, '创建成功')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()