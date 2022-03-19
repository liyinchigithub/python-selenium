from Chapter_12.Storm_12_1.PageObject.redmine_locators import *


class BasePage():
    # 构造一个基础类
    def __init__(self, driver):
        # 在初始化的时候，会自动运行
        self.driver = driver


class LoginPage(BasePage):
    # 用户登录页面的元素操作
    def enter_username(self, username):
        # 输入用户名
        ele = self.driver.find_element(*LoginPageLocators.UserName)
        ele.clear()
        ele.send_keys(username)

    def enter_password(self, password):
        # 输入密码
        ele = self.driver.find_element(*LoginPageLocators.PassWord)
        ele.send_keys(password)

    def click_login_button(self):
        # 点击登录按钮
        ele = self.driver.find_element(*LoginPageLocators.LoginButton)
        ele.click()

    def find_login_name(self):
        # 查找并返回登录后的用户名元素
        ele = self.driver.find_element(*LoginPageLocators.LoginName)
        return ele

    def find_login_failed_info(self):
        # 查找并返回登录失败后的提示信息元素
        ele = self.driver.find_element(*LoginPageLocators.LoginFailedInfo)
        return ele


class ProjectListPage(BasePage):
    # 项目列表页面元素的操作
    def click_new_pro_btn(self):
        # 点击新建项目按钮
        ele = self.driver.find_element(*ProjectListPageLocators.NewProject)
        ele.click()


class NewProjectPage(BasePage):
    # 新建项目页面的元素操作
    def enter_projectname(self, proname):
        # 输入项目名称
        ele = self.driver.find_element(*NewProjectPageLocators.ProjectName)
        ele.send_keys(proname)

    def click_com_btn(self):
        # 点击提交按钮
        ele = self.driver.find_element(*NewProjectPageLocators.CommitButton)
        ele.click()

    def get_pro_commit_info(self):
        # 获取提交项目后的提示信息
        ele = self.driver.find_element(*NewProjectPageLocators.ProjectCommitInfo)
        return ele