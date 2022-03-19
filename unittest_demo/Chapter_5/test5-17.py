from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
html_file = os.getcwd() + os.sep + 'myhtml5-1.html'
driver.get(html_file) # 绝对路径+HTML文件
# driver.get('d:\\Love\\Chapter-5\\test5-1.html') # 绝对路径+HTML文件
ele = driver.find_element_by_tag_name('input') # 通过tag name定位元素
ele.send_keys('storm')
sleep(2)
driver.quit()