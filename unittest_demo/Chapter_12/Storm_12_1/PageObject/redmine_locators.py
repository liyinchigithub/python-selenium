from selenium.webdriver.common.by import By

class LoginPageLocators():
    '''
    用户登录页
    '''
    UserName = (By.ID, 'username') # 登录名
    PassWord = (By.ID, 'password') # 登录密码
    LoginButton = (By.ID, 'login-submit') # 登录按钮
    LoginName = (By.ID, 'loggedas') # 登录后的用户名
    LoginFailedInfo = (By.ID, 'flash_error') # 登录失败后的信息


class ProjectListPageLocators():
    '''
    项目列表页面
    '''
    NewProject = (By.LINK_TEXT, '新建项目') # 新建项目按钮

class NewProjectPageLocators():
    '''
    新建项目页面
    '''
    ProjectName = (By.ID, 'project_name') # 项目名称
    CommitButton = (By.NAME, 'commit') # 提交按钮
    ProjectCommitInfo = (By.ID, 'flash_notice') # 提交后的信息