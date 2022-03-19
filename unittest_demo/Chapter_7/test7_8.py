from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml7-1.html'
driver.get(html_file)
driver.find_element_by_class_name('hello storm').send_keys('Storm')
sleep(2)
driver.quit()