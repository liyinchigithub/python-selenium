from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml6-8.html'
driver.get(html_file)
driver.find_element_by_id('kw').send_keys('storm') # 尝试定位搜索框，输入文字
sleep(2)
driver.quit()