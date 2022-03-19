'''
登录页
'''
# 页面元素对象层
class LoginPage(object):
    def __init__(self, driver):
        # 私有方法
        self.driver = driver

    def find_username(self):
        # 查找并返回用户名输入框元素
        ele = self.driver.find_element_by_id('username')
        return ele

    def find_password(self):
        # 查找并返回密码输入框元素
        ele = self.driver.find_element_by_id('password')
        return ele

    def find_login_btn(self):
        # 查找并返回登录按钮元素
        ele = self.driver.find_element_by_id('login-submit')
        return ele

    def find_login_name(self):
        # 查找并返回登录后的用户名元素
        ele = self.driver.find_element_by_id('loggedas')
        return ele

    def find_login_failed_info(self):
        # 查找并返回登录失败后的提示信息元素
        ele = self.driver.find_element_by_id('flash_error')
        return ele

# 页面元素操作层
class LoginOper(object):
    def __init__(self, driver):
        # 私有方法，调用元素定位的类
        self.login_page = LoginPage(driver)

    def input_username(self, username):
        # 对用户名输入框做clear和send_keys操作
        self.login_page.find_username().clear()
        self.login_page.find_username().send_keys(username)

    def input_password(self, password):
        # 对密码输入框做clear和send_keys操作
        self.login_page.find_password().clear()
        self.login_page.find_password().send_keys(password)

    def click_login_btn(self):
        # 对登录按钮做点击操作
        self.login_page.find_login_btn().click()

    def get_login_name(self):
        # 返回登录后的用户名元素的文字
        return self.login_page.find_login_name().text

    def get_login_failed_info(self):
        # 返回登录失败后提示信息的文字
        return self.login_page.find_login_failed_info().text

# 页面业务场景层
class LoginScenario(object):
    def __init__(self, driver):
        # 私有方法：调用页面元素操作
        self.login_oper = LoginOper(driver)

    def login(self, username, password):
        # 定义一个登录场景，用到了3个操作
        self.login_oper.input_username(username)
        self.login_oper.input_password(password)
        self.login_oper.click_login_btn()