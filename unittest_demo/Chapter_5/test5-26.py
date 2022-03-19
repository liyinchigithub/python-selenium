from selenium import webdriver
from time import sleep
import os

'''
串联查找的方式
'''
driver = webdriver.Chrome()
html_file = os.getcwd() + os.sep + 'myhtml5-2.html'
driver.get(html_file)
mytext = driver.find_element_by_id('B').find_element_by_tag_name('div').text
print(mytext)
driver.quit()
