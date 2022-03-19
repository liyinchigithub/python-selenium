from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml6-13.html'
driver.get(html_file)
sleep(2)
driver.find_element_by_tag_name('a').click()
sleep(5)
driver.quit()