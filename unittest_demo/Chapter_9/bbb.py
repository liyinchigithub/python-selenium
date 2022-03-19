from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
# 访问登录页
driver.get('http://localhost:81/redmine/login')
# 用例一：错误的密码登录失败
driver.find_element_by_id('username').clear()
driver.find_element_by_id('username').send_keys('admin')
driver.find_element_by_id('password').clear()
driver.find_element_by_id('password').send_keys('error')
driver.find_element_by_id('login-submit').click()
if '无效的用户名或密码1' in driver.page_source:
    print('pass')
else:
    print('fail')
# 用例二：正确的密码登录成功
driver.find_element_by_id('username').clear()
driver.find_element_by_id('username').send_keys('admin')
driver.find_element_by_id('password').clear()
driver.find_element_by_id('password').send_keys('rootroot1')
driver.find_element_by_id('login-submit').click()
login_name = driver.find_element_by_link_text('admin').text
if login_name == 'admin':
    print('pass')
else:
    print('fail')

driver.quit()