from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml6-12.html'
driver.get(html_file)
sleep(2)
driver.find_element_by_tag_name('input').send_keys('002020/06/06')
sleep(5)
driver.quit()