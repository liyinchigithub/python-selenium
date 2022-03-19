'''
项目列表页
'''

# 页面对象层
class ProjectListPage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_new_pro_btn(self):
        ele = self.driver.find_element_by_link_text('新建项目')
        return ele

# 对象操作层
class ProjectListOper(object):
    def __init__(self, driver):
        self.project_list_page = ProjectListPage(driver)

    def click_new_pro_btn(self):
        self.project_list_page.find_new_pro_btn().click()

# 业务逻辑层
class ProjectListScenario(object):
    def __init__(self, driver):
        self.project_list_oper = ProjectListOper(driver)

    def xxx(self):
        # 目前不需要封装业务逻辑
        pass