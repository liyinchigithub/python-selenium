'''
项目创建页
'''

# 页面对象层
class ProjectNewPage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_pro_name_input(self):
        ele = self.driver.find_element_by_id('project_name')
        return ele

    def find_pro_commit_btn(self):
        ele = commit_btn = self.driver.find_element_by_name('commit')
        return ele

    def find_pro_commit_info(self):
        ele = self.driver.find_element_by_id('flash_notice')
        return ele

# 对象操作层
class ProjectNewOper(object):
    def __init__(self, driver):
        self.project_new_page = ProjectNewPage(driver)

    def input_pro_name(self, pro_name):
        self.project_new_page.find_pro_name_input().send_keys(pro_name)

    def click_pro_commit_btn(self):
        self.project_new_page.find_pro_commit_btn().click()

    def get_pro_commit_info(self):
        return self.project_new_page.find_pro_commit_info().text


# 业务逻辑层
class ProjectNewScenario(object):
    def __init__(self, driver):
        self.project_new_oper = ProjectNewOper(driver)

    def new_project(self, pro_name):
        self.project_new_oper.input_pro_name(pro_name)
        self.project_new_oper.click_pro_commit_btn()