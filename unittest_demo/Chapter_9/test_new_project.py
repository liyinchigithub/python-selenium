from selenium import webdriver
import time

# 通过时间戳，构造唯一project name
project_name = 'project_{}'.format(time.time())
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
# 访问登录页
driver.get('http://localhost:81/redmine/login')
# 登录
login_name = driver.find_element_by_id('username')
login_name.clear()
login_name.send_keys('admin')
login_pwd = driver.find_element_by_id('password')
login_pwd.clear()
login_pwd.send_keys('rootroot')
login_btn = driver.find_element_by_id('login-submit')
login_btn.click()
# 访问项目列表页
driver.get('http://localhost:81/redmine/projects')
# 新建项目按钮
new_project = driver.find_element_by_link_text('新建项目')
new_project.click()
# 输入项目名称
pj_name = driver.find_element_by_id('project_name')
pj_name.send_keys(project_name)
# 提交按钮
commit_btn = driver.find_element_by_name('commit')
commit_btn.click()
# 新建项目成功后的提示信息
ele = driver.find_element_by_id('flash_notice')
if ele.text == '创建成功':
    print('pass')
else:
    print('fail')
driver.quit()