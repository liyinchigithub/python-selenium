from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml6-8.html'
driver.get(html_file)
driver.switch_to.frame('iframe1')  # 通过id切换
# driver.switch_to.frame('name1')  # 通过name切换
# driver.switch_to.frame(0) # 通过index切换
driver.find_element_by_id('kw').send_keys('storm') # 尝试定位搜索框，输入文字
sleep(2)
driver.quit()