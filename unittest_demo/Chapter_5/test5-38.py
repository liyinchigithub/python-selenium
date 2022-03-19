from selenium import webdriver
from time import sleep
import os

"""
判断页面元素是否可用
"""
driver = webdriver.Chrome()
html_file = os.getcwd() + os.sep + 'myhtml5-14.html'
driver.get(html_file)
ele1 = driver.find_element_by_id('input1')
ele2 = driver.find_element_by_id('input2')
ele3 = driver.find_element_by_id('input3')

# 可以通过is_enabled()方法判断页面元素是否可用；
# 如果页面元素有“disabled”属性的话，则页面元素不可用
print("ele1 is enabled {}".format(ele1.is_enabled()))
print("ele2 is enabled {}".format(ele2.is_enabled()))
print("ele3 is enabled {}".format(ele3.is_enabled()))

driver.quit()