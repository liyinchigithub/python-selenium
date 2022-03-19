from selenium import webdriver
from Chapter_12.Storm_12_1.PageObject import redmine_operations


class LoginScenario(object):
    '''
    这里定义登录页面的场景
    '''
    def redmine_login(self):
        # 场景一：登录成功
        url = 'http://localhost:81/redmine/login'
        username1 = "admin"
        password1 = "rootroot"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get(url)
        redmine_operations.LoginPage(driver).enter_username(username1)
        redmine_operations.LoginPage(driver).enter_password(password1)
        redmine_operations.LoginPage(driver).click_login_button()
        return driver

if __name__ == '__main__':
    LoginScenario().redmine_login()