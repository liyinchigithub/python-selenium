from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

'''
切到iframe，然后通过tab键定位到富文本框，输入
'''

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
# 第一个坑：定位收件人输入框的时候，要定位到input标签，否则不能使用send_keys
driver.find_element_by_class_name('nui-editableAddr-ipt').send_keys('apitest666@163.com')
# 第二个坑：需要组元素定位，通过下标取具体元素
ele = driver.find_elements_by_class_name('nui-ipt-input')[2]
ele.send_keys('邮件主题-Storm')
ele.send_keys(Keys.CONTROL, 'a')
ele.send_keys(Keys.CONTROL, 'c')
ele.send_keys(Keys.TAB)
sleep(3)
# 第三个坑：这里注意，不要ele.send_keys()
ActionChains(driver).send_keys('Hello Storm').perform()
sleep(3)
driver.quit()