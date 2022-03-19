from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml6-14.html'
driver.get(html_file)
sleep(2)
driver.find_element_by_id('file').send_keys("D:\\A\\storm.rar")  # 直接传递一个文件
sleep(3)
driver.quit()
