from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import os

driver = webdriver.Chrome()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml6-7.html'
driver.get(html_file)
s1 = Select(driver.find_element_by_id('s1'))
sleep(2)
s1.select_by_index(1)
sleep(2)
driver.quit()