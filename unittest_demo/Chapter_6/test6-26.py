from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml6-8.html'
driver.get(html_file)
driver.switch_to.frame(0) # 切到第一个iframe
driver.find_element_by_id('kw').send_keys('Storm') # 输入“Storm”
# driver.switch_to.parent_frame()  # 切回上一级页面
driver.switch_to.default_content() # 直接切回主页面
sleep(2)
driver.switch_to.frame(1) # 切到第二个iframe
driver.find_element_by_id('kw').send_keys('Shadow') # 输入“Shadow”

sleep(2)
driver.quit()