from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

'''
打开百度，在搜索框输入文字“storm”
通过复合按键ctrl+a全选
通过复合按键ctrl+c复制
通过clear()方法清除输入框中的内容
然后，通过复合按键ctrl+v粘贴，刚才复制的内容
'''
driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
# 通过send_keys() 模拟键盘输入文字
driver.find_element_by_id('kw').send_keys('storm')
sleep(3)
# 通过Keys.xxx模拟功能按键的操作
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'c')
# 通过clear()方法清除输入框中的内容
driver.find_element_by_id('kw').clear()
sleep(3)
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'v')
sleep(3)
driver.quit()