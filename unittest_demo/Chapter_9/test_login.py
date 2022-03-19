from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
# 访问登录页
driver.get('http://localhost:81/redmine/login')
# 用例一：错误的密码登录失败
# 登录名
login_name = driver.find_element_by_id('username')
login_name.clear()
login_name.send_keys('admin')
# 登录密码
login_pwd = driver.find_element_by_id('password')
login_pwd.clear()
login_pwd.send_keys('error')
# 登录按钮
login_btn = driver.find_element_by_id('login-submit')
login_btn.click()
# 登录失败后的提示信息
ele = driver.find_element_by_id('flash_error')
if '无效的用户名或密码' in driver.page_source:
    print('pass')
else:
    print('fail')
# 用例二：正确的密码登录成功
# 登录名
login_name = driver.find_element_by_id('username')
login_name.clear()
login_name.send_keys('admin')
# 登录密码
login_pwd = driver.find_element_by_id('password')
login_pwd.clear()
login_pwd.send_keys('rootroot')
# 登录按钮
login_btn = driver.find_element_by_id('login-submit')
login_btn.click()
# 登录后显示的用户名
name = driver.find_element_by_link_text('admin')
# 断言
if name.text == 'admin':
    print('pass')
else:
    print('fail')
driver.quit()