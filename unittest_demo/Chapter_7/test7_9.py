from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml7-1.html'
driver.get(html_file)
# 使用空格前或后面的部分来定位
driver.find_element_by_class_name('hello').send_keys('Storm')
sleep(2)
driver.quit()