from selenium import webdriver
from time import sleep
import os

'''
定位元素，通过text取文本；
'''
driver = webdriver.Chrome()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml7_3.html'
driver.get(html_file)
ele = driver.find_element_by_id('span_id')
print(ele.text)
driver.quit()