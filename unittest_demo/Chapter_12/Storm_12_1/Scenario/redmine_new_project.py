from Chapter_12.Storm_12_1.PageObject.redmine_operations import *
from Chapter_12.Storm_12_1.Scenario.redmine_login import *
import time

class NewProjectScenario(object):
    '''
    定义新建项目页面场景
    '''
    def redmine_new_project(self):
        # 通过时间戳，构造唯一project name
        project_name = 'project_{}'.format(time.time())
        # 登录
        driver = LoginScenario().redmine_login() # 登录
        # 访问项目列表页
        driver.get('http://localhost:81/redmine/projects')
        # 新建项目按钮
        ProjectListPage(driver).click_new_pro_btn()
        NewProjectPage(driver).enter_projectname(project_name)
        NewProjectPage(driver).click_com_btn()
        return driver