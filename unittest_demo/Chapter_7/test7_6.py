from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://mail.163.com/')
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element_by_id('switchAccountLogin').click()
driver.switch_to.frame(0)   #然后切到这个 iframe 页面
driver.find_element_by_name('email').send_keys('apitest333@163.com')
driver.find_element_by_name('password').send_keys('abcd1234')
driver.find_element_by_id('dologin').click()
sleep(13)
# 点击写信按钮
driver.find_elements_by_class_name('oz0')[1].click()
sleep(3)
# 富文本框在iframe中，要切
driver.switch_to.frame(3)
# 向元素中输入文字："document.getElementsByTagName('body')[0].innerHTML='<b>正文<b>;'"
js = "document.getElementsByTagName('body')[0].innerHTML='中国'"
driver.execute_script(js)
sleep(5)
driver.quit()