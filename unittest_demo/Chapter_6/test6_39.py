from selenium import webdriver
from time import sleep
import os

driver = webdriver.Firefox()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml6-14.html'
driver.get(html_file)
sleep(2)
ele = driver.find_element_by_id('file')
ele.click()
sleep(2)
driver.quit()


