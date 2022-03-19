from selenium import webdriver
import time,unittest


# 通过时间戳，构造唯一project name
project_name = 'project_{}'.format(time.time())

class TestNewProject(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        # 访问登录页
        self.driver.get('http://localhost:81/redmine/login')
        # 登录
        login_name = self.driver.find_element_by_id('username')
        login_name.clear()
        login_name.send_keys('admin')
        login_pwd = self.driver.find_element_by_id('password')
        login_pwd.clear()
        login_pwd.send_keys('rootroot')
        login_btn = self.driver.find_element_by_id('login-submit')
        login_btn.click()

    def test_new_project(self):
        # 访问项目列表页
        self.driver.get('http://localhost:81/redmine/projects')
        # 新建项目按钮
        new_project = self.driver.find_element_by_link_text('新建项目')
        new_project.click()
        # 输入项目名称
        pj_name = self.driver.find_element_by_id('project_name')
        pj_name.send_keys(project_name)
        # 提交按钮
        commit_btn = self.driver.find_element_by_name('commit')
        commit_btn.click()
        # 新建项目成功后的提示信息
        ele = self.driver.find_element_by_id('flash_notice')
        self.assertEqual(ele.text, '创建成功')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()